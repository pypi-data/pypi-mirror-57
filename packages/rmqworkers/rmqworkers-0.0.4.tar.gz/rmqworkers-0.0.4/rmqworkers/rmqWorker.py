"""Create a Client class"""

import threading
import multiprocessing
from os import getenv, path, mkdir

from rmqworkers.connection import Connection
from rmqworkers.errors import UnexpectedRabbitMQWorkerNoException, UnexpectedRunningTypeException
from rmqworkers.rmqWorker import *
from rmqworkers.logs import return_a_logger
from tempfile import gettempdir, NamedTemporaryFile

temp_dir = path.join(gettempdir(), __name__.split('.')[0])
try:
    mkdir(temp_dir)
except:
    pass
LOG = return_a_logger(temp_dir)

running_types = ['thread', 'process']


class Workers:
    def __init__(self, queues, running_type=getenv('RABBITMQ_RUNNING_TYPE', 'thread'), standalone=False):
        def thread():
            list_of_process = []
            no_of_workers = getenv('RABBITMQ_WORKERS', '300')
            if not no_of_workers.isdigit():
                LOG.error(f'Please use an integer value for RABBITMQ_WORKERS environment variable')
                raise UnexpectedRabbitMQWorkerNoException(status_code='87',
                                                          message='Please use an integer value for number of rmqworkers')
            for i in range(int(no_of_workers)):
                list_of_process.append(threading.Thread(target=Connection,
                                                        args=(queues)))
            LOG.info(f'The number of workers are: {len(list_of_process)} workers')
            for p in list_of_process:
                p.start()
                if self.standalone:
                    p.join()

        def process():
            list_of_process = []
            no_of_workers = getenv('RABBITMQ_WORKERS', '300')
            if not no_of_workers.isdigit():
                raise UnexpectedRabbitMQWorkerNoException(status_code='87',
                                                          message='Please use an integer value for number of rmqworkers')
            for i in range(int(no_of_workers)):
                list_of_process.append(multiprocessing.Process(target=Connection,
                                                               args=(queues)))
            LOG.info(f'The number of workers are: {len(list_of_process)} workers')
            for p in list_of_process:
                p.start()
                if self.standalone:
                    p.join()

        self.standalone = standalone
        LOG.info('The workers starting up...')
        LOG.info(f'The workers use queues: {queues}')
        LOG.info(f'The workers are running_type: {running_type}')
        LOG.info(f'The workers are running as standalone: {standalone}')
        if not running_type in running_types:
            LOG.error(f'Please use a value from {running_types} for RABBITMQ_RUNNING_TYPE environment variable')
            raise UnexpectedRunningTypeException(status_code='421',
                                                 message=f'Please use a value from {running_types}')
        if running_type == 'process':
            process()
        elif running_type == 'thread':
            thread()
        else:
            LOG.error('Please use a valid RABBITMQ_RUNNING_TYPE like "process" or "thread"')

