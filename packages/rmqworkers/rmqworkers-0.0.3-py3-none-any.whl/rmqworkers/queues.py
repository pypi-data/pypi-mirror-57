"""
This file have classes used for creating the required structure
"""

import logging

LOG = logging.getLogger('rmqworkers')


class BaseQueue:
    _instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance
