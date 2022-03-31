from utility.config import config

from abstractions.logger import AbstractLogger

from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine
from models.engine import Engine


class DrivingProcessor(AbstractDrivingProcessor):
    def __init__(self,
                 engine: AbstractEngine,
                 logger: AbstractLogger,
                 accelerationRatio=config.DefaultAccelerationRatio(),
                 maxAccelerationRatio=config.DefaultMaxAccelerationRatio(),
                 minAccelerationRatio=config.DefaultMinAccelerationRatio(),
                 maxSpeed=config.DefaultMaxSpeed(),
                 brakingSpeed=config.DefaultBrakingSpeed(),
                 ):

        # set initial speed to zero
        # TODO: introduce exception handling for min and max accelerationRatio
        # and max speed
        self.__maxSpeed: int = maxSpeed
        self.__brakingSpeed: int = brakingSpeed
        self.__actualSpeed: int = 0

        # consumption on init is 0
        self.__lastConsumption: float = 0

        if accelerationRatio < minAccelerationRatio:
            accelerationRatio = minAccelerationRatio

        if accelerationRatio > maxAccelerationRatio:
            accelerationRatio = maxAccelerationRatio

        self.__engine: AbstractEngine = engine
        self.__accelerationRatio: float = accelerationRatio
        self.__max_acceleration_ratio: float = maxAccelerationRatio
        self.__min_acceleration_ratio: float = minAccelerationRatio
        self.__logger = logger

    @property
    def ActualSpeed(self) -> int:
        self.__logger.log("Access actual car speed in driving processor.")
        return self.__actualSpeed

    @property
    def LastConsumption(self) -> float:
        self.__logger.log("Access last consumption in driving proccessor.")
        return self.__lastConsumption

    def CalculateConsumptionRate(self,
                                 isAccelerating: bool = False,
                                 isBraking: bool = False) -> float:
        currentSpeed = self.ActualSpeed
        consumption: float = 0

        self.__logger.log("Calculating consumption rate in driving proccesor.")

        if currentSpeed > 0:
            if currentSpeed < self.__get_car_maxspeed__ * 0.25:
                consumption = config.DefaultRunningQuaterConsumptionRate()
            elif currentSpeed < self.__get_car_maxspeed__ * 0.5:
                consumption = config.DefaultRunningHalfConsumptionRate()
            elif currentSpeed < self.__get_car_maxspeed__ * 0.75:
                consumption = config.DefaultRunningHalfConsumptionRate()
            elif currentSpeed < self.__get_car_maxspeed__:
                consumption = config.DefaultRunningUpperHalfConsumptionRate()
            elif currentSpeed == config.DefaultMaxSpeed():
                consumption = config.DefaultRunningMaxSpeedConsumptionRate()
        else:
            consumption = 0

        if isAccelerating:
            consumption *= config.DefaultAcceleratingCoefficient()
        elif isBraking:
            consumption *= config.DefaultBrakingCoefficient()

        self.__lastConsumption = consumption * config.DefaultCarCoefficient()
        return self.__lastConsumption

    def IncreaseSpeedTo(self, speed: int) -> None:
        self.__logger.log(f"Increasing speed by {speed} in driving proccesor.")
        if not self.__get_car_engine__.IsRunning:
            return

        # exception???
        if speed < self.__actualSpeed:
            self.__actualSpeed -= 1

        if self.__actualSpeed < speed:
            self.__actualSpeed = min(speed, self.__actualSpeed +
                                     self.__get_car_acceleration_ratio__)

        if self.__actualSpeed > self.__get_car_maxspeed__:
            self.__actualSpeed = self.__get_car_maxspeed__

        self.__get_car_engine__.Consume(self.CalculateConsumptionRate(True))

    def ReduceSpeedBy(self, reduceBy: int) -> None:
        self.__logger.log(f"Reducing speed by {reduceBy} km/h in driving pro.")
        if not self.__get_car_engine__.IsRunning:
            return

        self.__actualSpeed -= min(reduceBy, self.__get_car_braking_speed__)

        if self.__actualSpeed < 0:
            self.__actualSpeed = 0

        self.__get_car_engine__.Consume(self.CalculateConsumptionRate(False, True))

    @property
    def __get_car_engine__(self) -> AbstractEngine:
        return self.__engine

    @property
    def __get_car_maxspeed__(self) -> int:
        return self.__maxSpeed

    @property
    def __get_car_braking_speed__(self) -> int:
        return self.__brakingSpeed

    @property
    def __get_car_acceleration_ratio__(self) -> int:
        return self.__accelerationRatio

    @property
    def __get_car_max_acceleration_ratio__(self) -> int:
        return self.__max_acceleration_ratio

    @property
    def __get_car_min_acceleration_ratio__(self) -> int:
        return self.__min_acceleration_ratio
