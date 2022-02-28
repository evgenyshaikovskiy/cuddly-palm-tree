from abc import ABC, abstractmethod


# class that represents 'proccesor' of vehicle
class AbstractDrivingProcessor(ABC):

    @property
    @abstractmethod
    def ActualSpeed(self):
        """Gets actual speed of vehicle.(int)"""

    @abstractmethod
    def IncreaseSpeedTo(self, speed: int):
        """Increase speed until certain 'speed' (in kilometrs per hour)"""

    @abstractmethod
    def ReduceSpeedBy(self, reduceBy: int):
        """Reduces speed to certain value 'speed'(in kilometers per hour)"""
