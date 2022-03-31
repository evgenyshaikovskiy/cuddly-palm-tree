from abstractions.logger import AbstractLogger
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank


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
            self.__get_fuel_tank__.Consume(liters)

            if self.__get_fuel_tank__.FillLevel == 0:
                self.Stop()

    @property
    def __get_fuel_tank__(self) -> AbstractFuelTank:
        return self.__fuelTank
