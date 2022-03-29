from abc import ABC, abstractmethod


# class that describes fuel tank behaviour
class AbstractFuelTank(ABC):

    @property
    @abstractmethod
    def FillLevel(self):
        """Indicates amount of fuel(in liters)"""

    @property
    @abstractmethod
    def IsOnReserve(self):
        """Boolean property which indicates whether
        amount of fuel is below certain border"""

    @property
    @abstractmethod
    def IsFull(self):
        """Indicates whether tank is full"""

    @abstractmethod
    def Consume(self, liters: float):
        """Updates amount of fuel"""

    @abstractmethod
    def Refuel(self, liters: float):
        """Updates amount of fuel."""
