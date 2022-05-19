from abstractions.logger import AbstractLogger

import logging as lg
import string


class Logger(AbstractLogger):
    def __init__(self):
        self.__is_logging = True

    @staticmethod
    def setup():
        lg.basicConfig(level=lg.INFO,
                       filename='app.log',
                       filemode='w')

    def log(self, message: string):
        if self.__is_logging:
            print(message)
            lg.info(message)

    def disable_logging(self):
        self.__is_logging = False

    def enable_logging(self):
        self.__is_logging = True
