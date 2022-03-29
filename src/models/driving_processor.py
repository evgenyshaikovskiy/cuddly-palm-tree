from config import config
from logger import logger

from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine


class DrivingProcessor(AbstractDrivingProcessor):
    def __init__(self,
                 engine: AbstractEngine,
                 accelerationRatio=config.DefaultAccelerationRatio(),
                 maxAccelerationRatio=config.DefaultMaxAccelerationRatio(),
                 minAccelerationRatio=config.DefaultMinAccelerationRatio(),
                 maxSpeed=config.DefaultMaxSpeed(),
                 brakingSpeed=config.DefaultBrakingSpeed()):

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

    @property
    def ActualSpeed(self) -> int:
        logger.log("Access actual car speed in driving processor class.")
        return self.__actualSpeed

    @property
    def LastConsumption(self) -> float:
        logger.log("Access last consumption in driving proccessor class.")
        return self.__lastConsumption

    def CalculateConsumptionRate(self,
                                 isAccelerating: bool = False,
                                 isBraking: bool = False) -> float:
        currentSpeed = self.ActualSpeed
        consumption: float = 0

        logger.log("Calculating consumption rate in driving proccesor class.")

        if currentSpeed > 0:
            if currentSpeed < self.__maxSpeed * 0.25:
                consumption = config.DefaultRunningQuaterConsumptionRate()
            elif currentSpeed < self.__maxSpeed * 0.5:
                consumption = config.DefaultRunningHalfConsumptionRate()
            elif currentSpeed < self.__maxSpeed * 0.75:
                consumption = config.DefaultRunningHalfConsumptionRate()
            elif currentSpeed < self.__maxSpeed:
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
        logger.log(f"Increasing speed by {speed} in driving proccesor class.")
        if not self.__engine.IsRunning:
            return

        # exception???
        if speed < self.__actualSpeed:
            self.__actualSpeed -= 1

        if self.__actualSpeed < speed:
            self.__actualSpeed = min(speed, self.__actualSpeed +
                                     self.__accelerationRatio)

        if self.__actualSpeed > self.__maxSpeed:
            self.__actualSpeed = self.__maxSpeed

        self.__engine.Consume(self.CalculateConsumptionRate(True))

    def ReduceSpeedBy(self, reduceBy: int) -> None:
        logger.log(f"Reducing speed by {reduceBy} in driving processor class.")
        if not self.__engine.IsRunning:
            return

        self.__actualSpeed -= min(reduceBy, self.__brakingSpeed)

        if self.__actualSpeed < 0:
            self.__actualSpeed = 0

        self.__engine.Consume(self.CalculateConsumptionRate(False, True))
