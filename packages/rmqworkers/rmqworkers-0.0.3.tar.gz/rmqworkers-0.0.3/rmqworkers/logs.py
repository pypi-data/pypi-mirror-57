import logging
import logging.handlers
import sys
from os.path import join

import urllib3


def return_a_logger(location, file_name='rmqworkers.log'):
    """
    return a logger

    :return: logger obj
    """

    urllib3.disable_warnings()

    logger = logging.getLogger('rmqworkers')
    logger.setLevel(logging.DEBUG)
    print(f"Logging in file {join(location, file_name)}")
    file_handler = logging.handlers.RotatingFileHandler(join(location, file_name), mode='a+',
                                                        maxBytes=2000000, backupCount=4)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stderr_handler = logging.StreamHandler(sys.stderr)
    file_handler.setLevel(logging.DEBUG)

    # set a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s <br>')
    formatter2 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add a formater
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter2)
    stderr_handler.setFormatter(formatter2)

    # add handler
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    logger.addFilter(stderr_handler)

    # return logger
    return logger
