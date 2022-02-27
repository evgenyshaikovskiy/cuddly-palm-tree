from abstractions.fuel_tank import AbstractFuelTank


class FuelTank(AbstractFuelTank):

    def __init__(self, fillLevel=20, tankSize=60, onReserveBorder=5):
        # declare private variables with float types
        self.__fillLevel: float
        self.__tankSize: float
        self.__onReserveBorder: float

        if fillLevel < 0:
            self.__fillLevel = 0

        if fillLevel > tankSize:
            fillLevel = tankSize

        self.__fillLevel = fillLevel
        self.__tankSize = tankSize

    @property
    def FillLevel(self):
        return self.__fillLevel

    @property
    def IsOnReserve(self):
        return self.__fillLevel < self.__onReserveBorder

    @property
    def IsFull(self):
        return self.__fillLevel == self.__tankSize

    def Consume(self, liters: float):
        self.__fillLevel -= liters
        self.__fillLevel = round(self.__fillLevel, 10)

        if self.__fillLevel < 0:
            self.__fillLevel = 0

    def Refuel(self, liters: float):
        self.__fillLevel += liters

        if self.__fillLevel > self.__tankSize:
            self.__fillLevel = self.__tankSize
