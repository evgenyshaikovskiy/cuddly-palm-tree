from abc import ABC, abstractmethod


# class that represents 'proccesor'
# of vehicle (could be represented as multiple electronic car tools)
class AbstractDrivingProcessor(ABC):

    @property
    @abstractmethod
    def ActualSpeed(self):
        """Gets actual speed of vehicle in km/h."""

    @property
    @abstractmethod
    def LastConsumption(self):
        """Gets last consumption in liters."""

    @abstractmethod
    def CalculateConsumptionRate(self,
                                 isAccelerating: bool = False,
                                 isBraking: bool = False):
        """Gets comsumption level based on coefficient and car actual speed"""

    @abstractmethod
    def IncreaseSpeedTo(self, speed: float):
        """Increase speed until certain 'speed' (in kilometrs per hour)"""

    @abstractmethod
    def ReduceSpeedBy(self, reduceBy: float):
        """Reduces speed to certain value 'speed'(in kilometers per hour)"""
