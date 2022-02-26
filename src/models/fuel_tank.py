from abstractions.fuel_tank import AbstractFuelTank


class FuelTank(AbstractFuelTank):

    def __init__(self, fillLevel=20, tankSize=60):
        if fillLevel < 0:
            self.__fillLevel = 0

        if fillLevel > tankSize:
            fillLevel = tankSize

        self.__fillLevel = fillLevel
        self.__tankSize = tankSize
