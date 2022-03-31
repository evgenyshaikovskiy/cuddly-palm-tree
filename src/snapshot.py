from abstractions.observer import Observer
from abstractions.vehicle import AbstractVehicle


class CarSnapshot(Observer):
    def __init__(self, car: AbstractVehicle) -> None:
        self.__car = car

    def Handle(self) -> None:
        self.driving_display = self.__car.__getattribute__('__ActualSpeed__')
        print(self.driving_display)
