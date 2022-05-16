from abc import ABC, abstractmethod
from abstractions.fuel_tank_display import AbstractFuelTankDisplay


class AbstractFuelTankDisplayFactory(ABC):
    @abstractmethod
    def create_fuel_tank_display(self) -> AbstractFuelTankDisplay:
        """Create's new instance of fuel tank display"""
