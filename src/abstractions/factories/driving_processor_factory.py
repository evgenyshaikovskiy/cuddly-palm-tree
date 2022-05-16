from abc import ABC, abstractmethod
from abstractions.driving_processor import AbstractDrivingProcessor


class AbstractFuelTankDisplayFactory(ABC):
    @abstractmethod
    def create_driving_processor(self) -> AbstractDrivingProcessor:
        """Create's new instance of driving processor."""
