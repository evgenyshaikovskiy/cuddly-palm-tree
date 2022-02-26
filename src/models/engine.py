from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank


# concrete realization of engine abstract class
class Engine(AbstractEngine):

    def __init__(self, fuelTank: AbstractFuelTank):
        self.__fuelTank: AbstractFuelTank = fuelTank
        self.__isRunning: bool = False

    # property for private boolean value
    @property
    def IsRunning(self):
        return self.__isRunning

    def Start(self):
        self.__isRunning = True

    def Stop(self):
        self.__isRunning = False

    def Consume(self, liters: float):
        if self.__isRunning:
            self.__fuelTank.Consume(liters)

            if self.__fuelTank.FillLevel == 0:
                self.Stop()
