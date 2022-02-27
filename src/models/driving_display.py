from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.driving_display import AbstractDrivingDisplay


class DrivingInformationDisplay(AbstractDrivingDisplay):

    def __init__(self, drivingProcessor: AbstractDrivingProcessor):
        self.__drivingProcessor = drivingProcessor

    @property
    def ActualSpeed(self):
        return self.__drivingProcessor.ActualSpeed
