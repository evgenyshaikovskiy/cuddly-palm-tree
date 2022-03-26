from logger import logger

from abstractions.fuel_tank import AbstractFuelTank
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.fuel_tank import AbstractFuelTank


class FuelTankDisplay(AbstractFuelTankDisplay):

    def __init__(self, fuelTank: AbstractFuelTank):
        self.__fuelTank = fuelTank

    @property
    def FillLevel(self):
        logger.log('Access fill level in fuel tank display class.')
        return round(self.__fuelTank.FillLevel)

    @property
    def IsOnReserve(self):
        logger.log('Check whether car is on reverse in tank display class.')
        return self.__fuelTank.IsOnReserve

    @property
    def IsFull(self):
        logger.log('Check whether fuel tank is full in tank display class.')
        return self.__fuelTank.IsFull
