from logger import logger

from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.driving_display import AbstractDrivingDisplay


class DrivingDisplay(AbstractDrivingDisplay):

    def __init__(self, drivingProcessor: AbstractDrivingProcessor):
        self.__drivingProcessor = drivingProcessor

    @property
    def ActualSpeed(self) -> int:
        logger.log("Access actual car speed in driving display class.")
        return self.__drivingProcessor.ActualSpeed

    @property
    def ActualConsumption(self) -> float:
        logger.log("Access actual consumption in driving display class.")
        return self.__drivingProcessor.LastConsumption
