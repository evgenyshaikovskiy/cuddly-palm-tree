from abc import ABCMeta, abstractclassmethod, abstractproperty


# class that describes fuel tank behaviour
class AbstractFuelTank():

    @abstractproperty
    def FillLevel():
        "Indicates amount of fuel(in liters)"

    @abstractproperty
    def IsOnReserve():
        """Boolean property which indicates whether
        amount of fuel is below certain border"""

    @abstractproperty
    def IsFull():
        """Indicates whether tank is full"""

    @abstractclassmethod
    def Consume(liters: float):
        """Updates amount of fuel"""

    @abstractclassmethod
    def Refuel(liters: float):
        """Updates amount of fuel."""
