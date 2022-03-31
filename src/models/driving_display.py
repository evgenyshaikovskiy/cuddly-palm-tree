from logger import Logger

from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.logger import AbstractLogger


class DrivingDisplay(AbstractDrivingDisplay):

    def __init__(self, drivingProcessor: AbstractDrivingProcessor,
                 logger: AbstractLogger):
        self.__drivingProcessor = drivingProcessor
        self.__logger = logger

    @property
    def ActualSpeed(self) -> int:
        self.__logger.log("Access actual car speed in driving display class.")
        return self.__get_driving_processor__.ActualSpeed

    @property
    def ActualConsumption(self) -> float:
        self.__logger.log("Access actual consumption in driving display class")
        return self.__get_driving_processor__.LastConsumption

    @property
    def __get_driving_processor__(self) -> AbstractDrivingProcessor:
        return self.__drivingProcessor
