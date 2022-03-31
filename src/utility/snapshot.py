from __future__ import with_statement
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.observer import Observer
from abstractions.vehicle import AbstractVehicle
from abstractions.logger import AbstractLogger

from utility.logger import Logger

from models.car import Car

class SnapshotService(Observer):
    def __init__(self, car: AbstractVehicle) -> None:
        self.__car: AbstractVehicle = car
        self.__logger: AbstractLogger = Logger()
        self.__driving_display: AbstractDrivingDisplay = self.__car.__getattribute__('__get_driving_display__')
        self.__fuel_tank_display: AbstractFuelTankDisplay = self.__car.__getattribute__('__get_fuel_tank_display__')
        self.__driving_processor: AbstractDrivingProcessor = self.__car.__getattribute__('__get_driving_processor__')
        self.__fuel_tank: AbstractFuelTank = self.__car.__getattribute__('__get_fuel_tank__')

        # additional fields help to recreate the car
        self.__initial_fill_level = None
        self.__initial_consumption_level = None

    def Handle(self) -> None:
        self.__logger.disable_logging()
        self.__save_car__()
        self.__logger.enable_logging()


    def __load_car(self) -> AbstractVehicle:
        return Car(self.__logger)

    def __save_car__(self) -> None:
        self.__initial_fill_level = self.__fuel_tank_display.FillLevel
        self.__initial_consumption_level = self.__driving_display.ActualConsumption

        with open('car_information.txt', 'w', encoding='UTF-8') as save:
            # first write constructor parameters
            save.write(str(self.__fuel_tank_display.FillLevel) + '\n')
            save.write(str(self.__driving_processor.__getattribute__('__get_car_max_acceleration_ratio__'))+ '\n')
            save.write(str(self.__fuel_tank.__getattribute__('__get_tank_size__'))+ '\n')
            save.write(str(self.__fuel_tank.__getattribute__('__get_on_reserve_border__'))+ '\n')
            save.write(str(self.__driving_processor.__getattribute__('__get_car_acceleration_ratio__'))+ '\n')
            save.write(str(self.__driving_processor.__getattribute__('__get_car_min_acceleration_ratio__'))+ '\n')
            save.write(str(self.__driving_processor.__getattribute__('__get_car_maxspeed__'))+ '\n')
            save.write(str(self.__driving_processor.__getattribute__('__get_car_braking_speed__'))+ '\n')

            # write changing parameters
            save.write(str(self.__driving_display.ActualSpeed)+ '\n')
            save.write(str(self.__driving_display.ActualConsumption)+ '\n')
            save.write(str(self.__car.EngineIsRunning))
