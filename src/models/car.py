from config import config
from snapshot import CarSnapshot

from abstractions.logger import AbstractLogger
from abstractions.vehicle import AbstractVehicle
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.observable import Observable
from abstractions.observer import Observer

from models.driving_display import DrivingDisplay
from models.driving_processor import DrivingProcessor
from models.fuel_tank import FuelTank
from models.fuel_tank_display import FuelTankDisplay
from models.engine import Engine


class Car(AbstractVehicle, Observable):
    def __init__(self,
                 logger: AbstractLogger,
                 fillLevel=config.DefaultFillLevel(),
                 maxAccelerationRation=config.DefaultMaxAccelerationRatio(),
                 tankSize=config.DefaultTankSize(),
                 onReserveBorder=config.DefaultOnReserveBorder(),
                 accelerationRatio=config.DefaultAccelerationRatio(),
                 minAccelerationRatio=config.DefaultMinAccelerationRatio(),
                 maxSpeed=config.DefaultMaxSpeed(),
                 brakingSpeed=config.DefaultBrakingSpeed()):

        self.__logger: AbstractLogger = logger
        self.__observers = []

        self.__fuelTank: AbstractFuelTank = FuelTank(self.__logger,
                                                     fillLevel,
                                                     tankSize,
                                                     onReserveBorder)

        self.__fuelTankDisplay: AbstractFuelTankDisplay = FuelTankDisplay(
            self.__fuelTank,
            self.__logger)

        self.__engine: AbstractEngine = Engine(self.__logger, self.__fuelTank)

        self.__drivingProcessor: AbstractDrivingProcessor = DrivingProcessor(
            self.__engine,
            self.__logger,
            accelerationRatio,
            maxAccelerationRation,
            minAccelerationRatio,
            maxSpeed,
            brakingSpeed)

        self.__drivingDisplay: AbstractDrivingDisplay = DrivingDisplay(
            self.__drivingProcessor,
            self.__logger)

    @property
    def EngineIsRunning(self):
        self.__logger.log("Checks whether engine is running in car class.")
        return self.__engine.IsRunning

    @property
    def __ActualSpeed__(self) -> int:
        return self.__drivingDisplay.ActualSpeed

    def EngineStart(self) -> None:
        self.__logger.log("Starts an engine in car class.")
        if not self.__engine.IsRunning and self.__fuelTank.FillLevel > 0:
            self.__engine.Start()

    def EngineStop(self) -> None:
        self.__logger.log("Stops an engine in car class.")
        if self.__engine.IsRunning:
            self.__engine.Stop()

    def RunningIdle(self) -> None:
        self.__logger.log("Running idle in car calss.")
        self.Notify()
        self.__engine.Consume(config.DefaultRunningIdleConsumptionRate())

    def FreeWheel(self) -> None:
        self.__logger.log("Free wheel in car class.")
        self.__drivingProcessor.ReduceSpeedBy(1)

    def BrakeBy(self, speed: int) -> None:
        self.__logger.log(f"Break by {speed} in car class.")
        self.__drivingProcessor.ReduceSpeedBy(speed)

    def Accelerate(self, speed: int) -> None:
        self.__logger.log(f"Accelerate by {speed} in car class")
        self.__drivingProcessor.IncreaseSpeedTo(speed)

    def Refuel(self, liters: float) -> None:
        self.__logger.log(f"Refuel by {liters} in car class")
        self.__fuelTank.Refuel(liters)

    def Subscribe(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def Unsubscribe(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def Notify(self) -> None:
        for item in self.__observers:
            item.Handle()

    def GetInformationOnCar(self):
        if self.EngineIsRunning:
            print('For current moment car engine is running')
        else:
            print('For current moment car engine is not running')

        print(f'Actual speed is  {self.__drivingDisplay.ActualSpeed}')
        print(f'Actual consumption {self.__drivingDisplay.ActualConsumption}')
        print(f'Actual fill level is {self.__fuelTankDisplay.FillLevel}')
