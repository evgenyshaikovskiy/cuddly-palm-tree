from abc import ABC, abstractmethod


# class that represents 'processor'
# of vehicle (could be represented as multiple electronic car tools)
class AbstractDrivingProcessor(ABC):

    @property
    @abstractmethod
    def actual_speed(self):
        """Gets actual speed of vehicle in km/h."""

    @property
    @abstractmethod
    def last_consumption(self):
        """Gets last consumption in liters."""

    @abstractmethod
    def calculate_consumption_rate(self, isAccelerating: bool = False, isBraking: bool = False):
        """Gets comsumption level based on coefficient and car actual speed"""

    @abstractmethod
    def increase_speed_to(self, speed: float):
        """Increase speed until certain 'speed' (in kilometers per hour)"""

    @abstractmethod
    def reduce_speed_by(self, reduceBy: float):
        """Reduces speed to certain value 'speed'(in kilometers per hour)"""
