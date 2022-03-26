from config import config
from logger import logger

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
                 fillLevel=config.DefaultFillLevel(),
                 maxAccelerationRation=config.DefaultMaxAccelerationRatio(),
                 tankSize=config.DefaultTankSize(),
                 onReserveBorder=config.DefaultOnReserveBorder(),
                 accelerationRatio=config.DefaultAccelerationRatio(),
                 minAccelerationRatio=config.DefaultMinAccelerationRatio(),
                 maxSpeed=config.DefaultMaxSpeed(),
                 brakingSpeed=config.DefaultBrakingSpeed()):

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
        logger.log('Starts an engine in car class.')
        if not self.__engine.IsRunning and self.__fuelTank.FillLevel > 0:
            self.__engine.Start()

    def EngineStop(self):
        logger.log('Stops an engine in car class.')
        if self.__engine.IsRunning:
            self.__engine.Stop()

    def RunningIdle(self):
        logger.log('Running idle in car calss.')
        self.__engine.Consume(config.DefaultRunningIdleConsumptionRate)

    def FreeWheel(self):
        logger.log('Free wheel in car class.')
        self.__drivingProcessor.ReduceSpeedBy(1)

    def BrakeBy(self, speed: int):
        logger.log(f'Break by {speed} in car class')
        self.__drivingProcessor.ReduceSpeedBy(speed)

    def Accelerate(self, speed: int):
        logger.log(f'Accelerate by {speed} in car class')
        self.__drivingProcessor.IncreaseSpeedTo(speed)

    def Refuel(self, liters: float):
        logger.log(f'Refuel by {liters} in car class')
        self.__fuelTank.Refuel(liters)

    def GetInformationOnCar(self):
        if self.EngineIsRunning:
            print('For current moment car engine is running')
        else:
            print('For current moment car engine is not running')

        print(f'''Actual speed is  {self.__drivingDisplay.ActualSpeed}
        Actual consumption is {self.__drivingDisplay.ActualConsumption}
        Actual fill level is {self.__fuelTankDisplay.FillLevel}''')
