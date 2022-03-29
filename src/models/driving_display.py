from logger import logger

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
        return self.__drivingProcessor.ActualSpeed

    @property
    def ActualConsumption(self) -> float:
        self.__logger.log("Access actual consumption in driving display class")
        return self.__drivingProcessor.LastConsumption
