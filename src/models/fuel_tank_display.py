from abc import ABCMeta, abstractproperty


# class that describes display of fuel tank
class FuelTankDisplay():

    __metaclass__ = ABCMeta

    @abstractproperty
    def FillLevel():
        """Indicates fill level(float)"""

    @abstractproperty
    def IsOnReserve():
        """Boolean value which indicates whether
        fuel is below certain border"""

    @abstractproperty
    def IsFull():
        """Boolean value which indicates whether tank is full"""
