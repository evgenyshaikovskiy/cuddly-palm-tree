from abc import ABC, abstractmethod
from abstractions.driving_display import AbstractDrivingDisplay


class AbstractFuelTankDisplayFactory(ABC):
    @abstractmethod
    def create_driving_display(self) -> AbstractDrivingDisplay:
        """Create's new instance of driving display."""
