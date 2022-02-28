from config import config
from abstractions.vehicle import AbstractVehicle
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.driving_processor import AbstractDrivingProcessor

from models.driving_display import DrivingDisplay
from models.driving_processor import DrivingProcessor
from models.fuel_tank import FuelTank
from models.fuel_tank_display import FuelTankDisplay
from models.engine import Engine


class Car(AbstractVehicle):
    def __init__(self,
                 fillLevel=config.DefaultFillLevel,
                 maxAccelerationRation=config.DefaultMaxAccelerationRatio,
                 tankSize=config.DefaultTankSize,
                 onReserveBorder=config.DefaultOnReserveBorder,
                 accelerationRatio=config.AccelerationRatio,
                 minAccelerationRatio=config.DefaultMinAccelerationRatio,
                 maxSpeed=config.DefaultMaxSpeed,
                 brakingSpeed=config.DefaultBrakingSpeed):

        self.__fuelTank: AbstractFuelTank = FuelTank(fillLevel,
                                                     tankSize,
                                                     onReserveBorder)

        self.__fuelTankDisplay: AbstractFuelTankDisplay = FuelTankDisplay(
            self.__fuelTank)

        self.__engine: AbstractEngine = Engine(self.__fuelTank)

        self.__drivingProcessor: AbstractDrivingProcessor = DrivingProcessor(
            self.__engine,
            accelerationRatio,
            maxAccelerationRation,
            minAccelerationRatio,
            maxSpeed,
            brakingSpeed)

        self.__drivingDisplay: AbstractDrivingDisplay = DrivingDisplay(
            self.__drivingProcessor)

    @property
    def EngineIsRunning(self):
        return self.__engine.IsRunning

    def EngineStart(self):
        if not self.__engine.IsRunning and self.__fuelTank.Fillevel > 0:
            self.__engine.Start()

    def EngineStop(self):
        if self.__engine.IsRunning:
            self.__engine.Stop()

    def RunningIdle(self):
        # consider refactoring this part
        self.__engine.Consume(0.003)

    def FreeWheel(self):
        self.__drivingProcessor.ReduceSpeedBy(1)

    def BrakeBy(self, speed: int):
        self.__drivingProcessor.ReduceSpeedBy(speed)

    def Accelerate(self, speed: int):
        self.__drivingProcessor.IncreaseSpeedTo(speed)

    def GetInformationOnCar(self):
        print(f'Vehicle actual speed is {self.__drivingDisplay.ActualSpeed}')
        # add compsumption
