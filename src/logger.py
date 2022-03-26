import logging as lg
import string


class logger():
    @staticmethod
    def setup():
        lg.basicConfig(level=lg.INFO,
                       filename='app.log',
                       filemode='w',
                       format='%(name)s - %(levelname)s - %message%s')

    @staticmethod
    def log(message: string):
        print(message)
        lg.log(message)
