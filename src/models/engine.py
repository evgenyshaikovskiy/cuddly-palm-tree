from abstractions.logger import AbstractLogger
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank


# concrete realization of engine abstract class
class Engine(AbstractEngine):

    def __init__(self, logger: AbstractLogger, fuelTank: AbstractFuelTank):
        self.__fuelTank: AbstractFuelTank = fuelTank
        self.__isRunning: bool = False
        self.__logger = logger

    @property
    def IsRunning(self) -> bool:
        self.__logger.log("Check whether car is running in engine class.")
        return self.__isRunning

    def Start(self) -> None:
        self.__logger.log("Start car engine in engine class.")
        self.__isRunning = True

    def Stop(self) -> None:
        self.__logger.log("Stop car engine in engine class.")
        self.__isRunning = False

    def Consume(self, liters: float) -> None:
        self.__logger.log(f"Consume {liters} liters in engine class.")
        if self.__isRunning:
            self.__fuelTank.Consume(liters)

            if self.__fuelTank.FillLevel == 0:
                self.Stop()
