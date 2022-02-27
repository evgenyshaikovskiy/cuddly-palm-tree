from abc import ABC, abstractmethod


# class that describes actual information on vehicle speed and other parameters
class AbstractDrivingDisplay(ABC):

    @property
    @abstractmethod
    def ActualSpeed(self):
        """Indicates actual speed of vehicle."""
