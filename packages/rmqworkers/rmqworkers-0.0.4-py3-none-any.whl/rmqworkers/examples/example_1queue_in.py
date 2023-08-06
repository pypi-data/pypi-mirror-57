import sys
import os

sys.path.append('..'+os.sep+'..'+os.sep)

from rmqworkers.rmqWorker import Workers
from rmqworkers.queues import BaseQueue
from os import getenv
import logging

LOG = logging.getLogger('rmqworkers')


class InQueue(BaseQueue):
    """
    In queue that needs to be used in your code
    """
    _instance = None  # must be here
    _type = 'in'  # a single in queue is permitted per Workers object
    queue_name = getenv('IN_QUE', 'in')
    priority = 1

    @staticmethod
    def work(message):
        """
        Every class that inherits BaseQueue has a work method that will be automatically called
        :param message: message object that needs to be consumed
        :return: None
        """
        try:
            msg = eval(message.body)
        except Exception as err:
            LOG.error(f'Unexpected Error: {str(err)} for message{repr(message.body)}')
        else:
            # change something.
            msg['job_info'] = msg['job_info'] + '!!!!!!!'
            LOG.info("Message was consumed: {}".format(msg))
            print("Message was consumed: {}".format(msg))
            message.ack()


# publish in queue in { "job_info": "11111"}
Workers(queues=(InQueue,), running_type='thread', standalone=True)
# read from out queue that you modified


class Student(object):
    def __init__(self,nume):
        self.__nume=str(nume)
    @property
    def nume(self):
        return self.__nume
    nume.setter
    def set_nume(self,nume):
        self.__nume=str(nume)

        nume.deleter
    def del_nume(self):
        del self.__nume