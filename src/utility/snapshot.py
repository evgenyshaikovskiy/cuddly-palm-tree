from __future__ import with_statement
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.observer import Observer
from abstractions.vehicle import AbstractVehicle
from abstractions.logger import AbstractLogger


class SnapshotService(Observer):
    def __init__(self):
        self.__car: AbstractVehicle = None

    def handle(self, car: AbstractVehicle, logger: AbstractLogger) -> None:
        self.__car = car
        logger.disable_logging()
        self.__save_car__()
        logger.enable_logging()

    def __save_car__(self) -> None:
        # get car parts
        self.__driving_display: AbstractDrivingDisplay = self.__car.__getattribute__('__get_driving_display__')
        self.__fuel_tank_display: AbstractFuelTankDisplay = self.__car.__getattribute__('__get_fuel_tank_display__')
        self.__driving_processor: AbstractDrivingProcessor = self.__car.__getattribute__('__get_driving_processor__')
        self.__fuel_tank: AbstractFuelTank = self.__car.__getattribute__('__get_fuel_tank__')

        with open('car_information.txt', 'w', encoding='UTF-8') as file:
            # first write constructor parameters
            file.write(str(self.__fuel_tank_display.fill_level) + '\n')
            file.write(str(self.__driving_processor.__getattribute__('__get_car_max_acceleration_ratio__')) + '\n')
            file.write(str(self.__fuel_tank.__getattribute__('__get_tank_size__')) + '\n')
            file.write(str(self.__fuel_tank.__getattribute__('__get_on_reserve_border__')) + '\n')
            file.write(str(self.__driving_processor.__getattribute__('__get_car_acceleration_ratio__')) + '\n')
            file.write(str(self.__driving_processor.__getattribute__('__get_car_min_acceleration_ratio__')) + '\n')
            file.write(str(self.__driving_processor.__getattribute__('__get_car_maxspeed__')) + '\n')
            file.write(str(self.__driving_processor.__getattribute__('__get_car_braking_speed__')) + '\n')

            # write changing parameters
            file.write(str(self.__driving_display.actual_speed) + '\n')
            file.write(str(self.__driving_display.actual_consumption) + '\n')
            file.write(str(self.__car.engine_is_running))
