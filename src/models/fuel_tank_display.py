from abstractions.fuel_tank import AbstractFuelTank
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.fuel_tank import AbstractFuelTank


class FuelTankDisplay(AbstractFuelTankDisplay):

    def __init__(self, fuelTank: AbstractFuelTank):
        self.__fuelTank = fuelTank

    @property
    def FillLevel(self):
        return round(self.__fuelTank.FillLevel)

    @property
    def IsOnReserve(self):
        return self.__fuelTank.IsOnReserve

    @property
    def IsFull(self):
        return self.__fuelTank.IsFull
