from abc import ABC, abstractmethod


# class that describes display of fuel tank
class FuelTankDisplay(ABC):

    @property
    @abstractmethod
    def FillLevel(self):
        """Indicates fill level(float)"""

    @property
    @abstractmethod
    def IsOnReserve(self):
        """Boolean value which indicates whether
        fuel is below certain border"""

    @property
    @abstractmethod
    def IsFull(self):
        """Boolean value which indicates whether tank is full"""
