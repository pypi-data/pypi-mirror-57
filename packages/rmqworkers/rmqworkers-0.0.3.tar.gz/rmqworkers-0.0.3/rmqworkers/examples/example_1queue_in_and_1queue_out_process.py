import sys

import os

sys.path.append('..'+os.sep+'..'+os.sep)
from amqpstorm import Message

from rmqworkers.rmqWorker import Workers
from rmqworkers.queues import BaseQueue
from os import getenv
import logging

LOG = logging.getLogger('rmqworkers')


class InQueue(BaseQueue):
    _instance = None  # must be here
    _type = 'in'  # a single in queue is permitted per Workers object
    queue_name = getenv('IN_QUE', 'in')
    priority = 1

    @staticmethod
    def work(message):
        """
        Extract work
        :param message:
        :return:k
        """
        try:
            msg = eval(message.body)
        except Exception as err:
            msg = message.body
            LOG.error('Unexpected Error:' + str(err))
        else:
            # change something.
            msg['job_info'] = msg['job_info'] + '!!!!!!!'
            LOG.info("Message was consumed: {}".format(msg))
            # send to out queue
            if InQueue.out_queues['out'].work(msg):
                message.ack()


class OutQueue(BaseQueue):
    """
    In queue that needs to be used in your code
    """
    _instance = None
    _type = 'out'
    routing = 'normal'
    queue_name = getenv('OUT_QUE', 'out')
    priority = 1

    @staticmethod
    def work(message):
        """
        Every class that inherits BaseQueue has a work method that will be automatically called
        :param message: message object that needs to be consumed
        :return: None
        """
        properties = {
            'priority': OutQueue.priority,
            'content_type': 'text/plain',
            'expiration': '3600',
            'headers': {'key': 'value'},
        }
        message['add_something'] = 'something'
        message_out = Message.create(channel=OutQueue.channel,
                                     body=str(message),
                                     properties={})
        message_out.publish(OutQueue.queue_name)
        LOG.info("Message was added in out queue: {}".format(message))
        return True


# publish in queue in { "job_info": "11111"}
Workers(queues=(InQueue, OutQueue), running_type='process', standalone=False)
# read from out queue that you modified
