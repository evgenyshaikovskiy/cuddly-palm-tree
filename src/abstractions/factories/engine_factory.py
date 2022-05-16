from abc import ABC, abstractmethod
from abstractions.engine import AbstractEngine


class AbstractFuelTankDisplayFactory(ABC):
    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        """Create's new instance of engine"""
