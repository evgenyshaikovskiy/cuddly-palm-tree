from abc import ABC, abstractmethod


# class that commonly describes all engines
class AbstractEngine(ABC):

    @property
    @abstractmethod
    def IsRunning(self):
        """Indicates whether engine is running"""

    @abstractmethod
    def Consume(self, liters: float):
        """Consumes certain amount of liters"""

    @abstractmethod
    def Start(self):
        """Starts an engine"""

    @abstractmethod
    def Stop(self):
        """Stops an engine"""
