from abc import ABC, abstractmethod

from abstractions.fuel_tank import AbstractFuelTank


class AbstractFuelTankDisplayFactory(ABC):
    @abstractmethod
    def create_fuel_tank(self) -> AbstractFuelTank:
        """Create's new instance of fuel tank."""
