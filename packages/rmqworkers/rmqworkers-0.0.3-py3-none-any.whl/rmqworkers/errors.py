"""
This file intend to be
"""


class UnexpectedQueueException(Exception):
    def __init__(self, status_code, message):
        super(UnexpectedQueueException, self).__init__(str(status_code) + " : " + str(message))


class UnexpectedRabbitMQWorkerNoException(Exception):
    def __init__(self, status_code, message):
        super(UnexpectedRabbitMQWorkerNoException, self).__init__(str(status_code) + " : " + str(message))


class UnexpectedRunningTypeException(Exception):
    def __init__(self, status_code, message):
        super(UnexpectedRabbitMQWorkerNoException, self).__init__(str(status_code) + " : " + str(message))
