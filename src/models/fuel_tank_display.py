from abstractions.logger import AbstractLogger
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.fuel_tank import AbstractFuelTank


class FuelTankDisplay(AbstractFuelTankDisplay):

    def __init__(self, fuelTank: AbstractFuelTank, logger: AbstractLogger):
        self.__fuelTank = fuelTank
        self.__logger = logger

    @property
    def FillLevel(self) -> float:
        self.__logger.log("Access fill level in fuel tank display.")
        return round(self.__fuelTank.FillLevel)

    @property
    def IsOnReserve(self) -> bool:
        self.__logger.log("Check whether car is on reverse in tank display.")
        return self.__fuelTank.IsOnReserve

    @property
    def IsFull(self) -> bool:
        self.__logger.log("Check whether fuel tank is full in tank display.")
        return self.__fuelTank.IsFull
