from abc import ABC, abstractmethod


from abstractions.vehicle import AbstractVehicle


class AbstractCarFactory(ABC):
    @abstractmethod
    def create_car(self) -> AbstractVehicle:
        """Return's actual car."""
