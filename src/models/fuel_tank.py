from logger import logger

from abstractions.fuel_tank import AbstractFuelTank
from config import config


class FuelTank(AbstractFuelTank):

    def __init__(self,
                 fillLevel=config.DefaultFillLevel(),
                 tankSize=config.DefaultTankSize(),
                 onReserveBorder=config.DefaultFillLevel()):
        self.__onReserveBorder: float = onReserveBorder

        if fillLevel < 0:
            self.__fillLevel = 0

        if fillLevel > tankSize:
            fillLevel = tankSize

        self.__fillLevel = fillLevel
        self.__tankSize = tankSize

    @property
    def FillLevel(self):
        logger.log('Access fill level in fuel tank class.')
        return self.__fillLevel

    @property
    def IsOnReserve(self):
        logger.log('Calculating whether car is on reverse in fuel tank class.')
        return self.__fillLevel < self.__onReserveBorder

    @property
    def IsFull(self):
        logger.log('Calculating whether fuel tank is full in fuel tank class.')
        return self.__fillLevel == self.__tankSize

    def Consume(self, liters: float):
        logger.log(f'Consuming {liters} liters in fuel tank class.')
        self.__fillLevel -= liters
        self.__fillLevel = round(self.__fillLevel, 10)

        if self.__fillLevel < 0:
            self.__fillLevel = 0

    def Refuel(self, liters: float):
        logger.log(f'Refuel tank by {liters} liters in fuel tank class.')
        self.__fillLevel += liters

        if self.__fillLevel > self.__tankSize:
            self.__fillLevel = self.__tankSize
