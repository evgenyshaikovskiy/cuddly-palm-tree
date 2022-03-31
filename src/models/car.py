from config import config

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
        return self.__get_engine__.IsRunning

    def EngineStart(self) -> None:
        self.__logger.log("Starts an engine in car class.")
        if not self.__get_engine__.IsRunning and self.__get_fuel_tank__.FillLevel > 0:
            self.__get_engine__.Start()

    def EngineStop(self) -> None:
        self.__logger.log("Stops an engine in car class.")
        if self.__get_engine__.IsRunning:
            self.__get_engine__.Stop()

    def RunningIdle(self) -> None:
        self.__logger.log("Running idle in car calss.")
        self.Notify()
        self.__get_engine__.Consume(config.DefaultRunningIdleConsumptionRate())

    def FreeWheel(self) -> None:
        self.__logger.log("Free wheel in car class.")
        self.__get_driving_processor__.ReduceSpeedBy(1)

    def BrakeBy(self, speed: int) -> None:
        self.__logger.log(f"Break by {speed} in car class.")
        self.__get_driving_processor__.ReduceSpeedBy(speed)

    def Accelerate(self, speed: int) -> None:
        self.__logger.log(f"Accelerate by {speed} in car class")
        self.__get_driving_processor__.IncreaseSpeedTo(speed)

    def Refuel(self, liters: float) -> None:
        self.__logger.log(f"Refuel by {liters} in car class")
        self.__get_fuel_tank__.Refuel(liters)

    def Subscribe(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def Unsubscribe(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def Notify(self) -> None:
        for item in self.__observers:
            item.Handle()

    def GetInformationOnCar(self) -> None:
        if self.EngineIsRunning:
            print('For current moment car engine is running')
        else:
            print('For current moment car engine is not running')

        print(f'Actual speed is  {self.__get_driving_display__.ActualSpeed}')
        print(f'Actual consumption {self.__get_driving_display__.ActualConsumption}')
        print(f'Actual fill level is {self.__get_fuel_tank_display__.FillLevel}')

    # private properties for reflection
    @property
    def __get_engine__(self) -> AbstractEngine:
        return self.__engine

    @property
    def __get_fuel_tank__(self) -> AbstractFuelTank:
        return self.__fuelTank

    @property
    def __get_fuel_tank_display__(self) -> AbstractFuelTankDisplay:
        return self.__fuelTankDisplay

    @property
    def __get_driving_display__(self) -> AbstractDrivingDisplay:
        return self.__drivingDisplay

    @property
    def __get_driving_processor__(self) -> AbstractDrivingProcessor:
        return self.__drivingProcessor
