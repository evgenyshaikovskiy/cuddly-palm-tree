from abstractions.logger import AbstractLogger
from models.car import Car
import string

class RestoreService():
    def __init__(self):
        # instantiate fields
        self.__fill_level: float = None
        self.__car_max_acceleration_ratio: float = None
        self.__tank_size: float = None
        self.__on_reserve_border: float = None
        self.__acceleration_ratio: float = None
        self.__min_acceleration_ratio: float = None
        self.__car_max_speed: float = None
        self.__braking_speed: float = None

        self.__actual_speed: float = None
        self.__actual_consumption: float = None
        self.__is_engine_running: bool = None

    def restore_car(self, logger: AbstractLogger) -> Car:
        # read file
        self.__read_file__()

        car: Car = Car(logger,
                       self.__get_fill_level__,
                       self.__get_car_max_acceleration_ratio__,
                       self.__get_tank_size__,
                       self.__on_reserve_border,
                       self.__acceleration_ratio,
                       self.__min_acceleration_ratio,
                       self.__car_max_speed,
                       self.__get_car_braking_speed__)
        
        return car

    def __read_file__(self) -> None:
        with open('car_information.txt', 'r') as file:
            self.__set_fill_level__(float(file.readline()))
            self.__set_car_max_acceleration_ratio(float(file.readline()))
            self.__set_tank_size__(float(file.readline()))
            self.__set_on_reserve_border__(float(file.readline()))
            self.__set_car_acceleration_ratio__(float(file.readline()))
            self.__set_car_min_acceleration_ratio__(float(file.readline()))
            self.__set_car_max_speed__(float(file.readline()))
            self.__set_car_braking_speed__(float(file.readline()))
            
            self.__set_car_actual_speed__(float(file.readline()))
            self.__set_car_actual_consumption__(float(file.readline()))

            # refactor this boolean
            is_engine_running: bool = None
            parsed_boolean: string = str(file.readline())
            if parsed_boolean == 'True':
                is_engine_running = True
            elif parsed_boolean == 'False':
                is_engine_running = False
            else:
                # exception
                print('Corrupted input')

            self.__set_is_engine_running__(is_engine_running)

    @property
    def __get_fill_level__(self) -> float:
        return self.__fill_level

    def __set_fill_level__(self, value: float) -> None:
        self.__fill_level = value

    @property
    def __get_car_max_acceleration_ratio__(self) -> float:
        return self.__car_max_acceleration_ratio

    def __set_car_max_acceleration_ratio(self, value: float) -> None:
        self.__car_max_acceleration_ratio = value

    @property
    def __get_tank_size__(self) -> float:
        return self.__tank_size

    def __set_tank_size__(self, value: float) -> None:
        self.__tank_size = value

    @property
    def __get_on_reserve_border__(self) -> float:
        return self.__on_reserve_border

    def __set_on_reserve_border__(self, value: float) -> None:
        self.__on_reserve_border = value

    @property
    def __get_car_acceleration_ratio__(self) -> float:
        return self.__acceleration_ratio

    def __set_car_acceleration_ratio__(self, value: float) -> None:
        self.__acceleration_ratio = value

    @property
    def __get_car_min_acceleration_ratio__(self) -> float:
        return self.__min_acceleration_ratio

    def __set_car_min_acceleration_ratio__(self, value: float) -> None:
        self.__min_acceleration_ratio = value

    @property
    def __get_car_max_speed__(self) -> float:
        return self.__car_max_speed

    def __set_car_max_speed__(self, value: float) -> None:
        self.__car_max_speed = value

    @property
    def __get_car_braking_speed__(self) -> float:
        return self.__braking_speed

    def __set_car_braking_speed__(self, value: float) -> None:
        self.__braking_speed = value

    @property
    def __get_car_actual_speed__(self) -> float:
        return self.__actual_speed

    def __set_car_actual_speed__(self, value: float) -> None:
        self.__actual_speed = value

    @property
    def __get_car_actual_consumption__(self) -> float:
        return self.__actual_consumption

    def __set_car_actual_consumption__(self, value: float):
        self.__actual_consumption = value

    @property
    def __get_is_engine_running__(self) -> bool:
        return self.__is_engine_running

    def __set_is_engine_running__(self, value: bool):
        self.__is_engine_running = value