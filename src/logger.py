from abstractions.logger import AbstractLogger

import logging as lg
import string


class Logger(AbstractLogger):
    def __init__(self):
        self.__isLogging = True

    @staticmethod
    def setup():
        lg.basicConfig(level=lg.INFO,
                       filename='app.log',
                       filemode='w')

    def log(self, message: string):
        if self.__isLogging:
            print(message)
            lg.info(message)

    def __disable_logging__(self):
        self.__isLogging = False

    def __enable_logging__(self):
        self.__isLogging = True
