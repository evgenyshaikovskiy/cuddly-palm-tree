from abc import ABCMeta, abstractclassmethod, abstractproperty


# class that commonly describes all engines
class AbstractEngine():

    __metaclass__ = ABCMeta

    @abstractproperty
    def IsRunning():
        """Indicates whether engine is running"""

    @abstractclassmethod
    def Consume(liters: float):
        """Consumes certain amount of liters"""

    @abstractclassmethod
    def Start():
        """Starts an engine"""

    @abstractclassmethod
    def Stop():
        """Stops an engine"""
