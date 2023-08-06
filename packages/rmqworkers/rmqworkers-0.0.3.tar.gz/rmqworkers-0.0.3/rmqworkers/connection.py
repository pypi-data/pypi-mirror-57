"""
Create and maintain connection
"""
import logging
from os import getenv
from random import randrange
from time import sleep

from amqpstorm import Connection as connect
from amqpstorm.management import ApiError
from amqpstorm.management.exception import ApiConnectionError

from rmqworkers import errors
from rmqworkers.queues import BaseQueue

LOG = logging.getLogger('rmqworkers')


class Connection:

    def __init__(self, *queues):
        if not all([issubclass(q, BaseQueue) for q in queues]):
            LOG.error('Please use proper queue.')

            raise errors.UnexpectedQueueException(status_code='124',
                                                  message='Please use a proper Queue class')
        in_queue = [q for q in queues if q._type == 'in']
        if len(in_queue) != 1:
            raise errors.UnexpectedQueueException(status_code='37',
                                                  message='Please add a single in Queue class as argument')

        self.in_queue = in_queue[0]
        self.queues = queues
        self.channel = None
        self.response = None
        self.connection = None
        self.callback_queue = None
        self.correlation_id = None

        self.create_connections()
        self.create_queue()
        self.create_consumer()

    def create_connections(self):
        """
        Create a connection for client
        :return:
        """
        LOG.info("Authentication started..")
        self.connection = connect(hostname=getenv('RABBITMQ_VIP', 'localhost'),
                                  username=getenv('RABBITMQ_USERNAME', 'guest'),
                                  password=getenv('RABBITMQ_PASSWORD', 'guest'),
                                  port=int(getenv('RABBITMQ_PORT', 5672)))
        self.connection.open()
        self.channel = self.connection.channel()
        for q in self.queues: q.channel = self.channel
        self.in_queue.out_queues = {q.queue_name: q for q in self.queues if q._type == 'out'}
        LOG.info("Connection through AMPQ with a controller created")

    def create_queue(self):
        while True:
            try:
                self.channel.exchange.declare(exchange='mlan', exchange_type='topic')
                for q in self.queues:
                    self.channel.queue.declare(q.queue_name, durable=True, arguments={'x-max-priority': 10,
                                                                                      'x-message-ttl': 500000,
                                                                                      'x-max-length': 20000})
                    self.channel.queue.bind(queue=q.queue_name, exchange="mlan", routing_key="normal",
                                            arguments={})

            except ApiError as why:
                LOG.info('Queue "failover" created', exc_info=True)

            except ApiConnectionError:
                LOG.error('Can\'t connect to rabbitMQ')
                raise Exception("Can't connect to RabbitMQ. Please provide real IP address, username and password")
            else:
                return
            sleep(1)

    def create_consumer(self):
        """
        Create consumer
        :param self:
        :return:
        """
        while True:
            try:
                LOG.info('Start consuming messages in order to extract from in queue.')
                sleep(float("1." + str(randrange(100))))
                self.channel.basic.consume(callback=self.in_queue.work, queue=self.in_queue.queue_name, no_ack=False)

                self.channel.start_consuming()
            except KeyboardInterrupt:
                self.channel.close()
                LOG.info('Program was closed. Bye!')
            except Exception as err:
                self.create_connections()
                LOG.warning('Channel was close doe to error:' + str(err), exc_info=True)
                LOG.warning("Reinitializate channel..")
            sleep(0.5)
