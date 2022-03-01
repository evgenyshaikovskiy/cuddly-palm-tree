from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine
from config import config


class DrivingProcessor(AbstractDrivingProcessor):
    def __init__(self,
                 engine: AbstractEngine,
                 accelerationRatio=config.DefaultAccelerationRatio(),
                 maxAccelerationRatio=config.DefaultMaxAccelerationRatio(),
                 minAccelerationRatio=config.DefaultMinAccelerationRatio(),
                 maxSpeed=config.DefaultMaxSpeed(),
                 brakingSpeed=config.DefaultBrakingSpeed(),
                 coefficient=config.DefaultCoefficient()):

        # set initial speed to zero
        # TODO: introduce exception handling for min and max accelerationRatio
        # and max speed
        self.__maxSpeed: int = maxSpeed
        self.__brakingSpeed: int = brakingSpeed
        self.__actualSpeed: int = 0
        self.__coefficient: float = coefficient

        if accelerationRatio < minAccelerationRatio:
            accelerationRatio = minAccelerationRatio

        if accelerationRatio > maxAccelerationRatio:
            accelerationRatio = maxAccelerationRatio

        self.__engine: AbstractEngine = engine
        self.__accelerationRatio: float = accelerationRatio

    @property
    def ActualSpeed(self):
        return self.__actualSpeed

    @property
    def CalculateConsumptionRate(self):
        currentSpeed = self.ActualSpeed
        consumption: float = 0
        if currentSpeed > 0:
            if currentSpeed < self.__maxSpeed * 0.25:
                consumption = config.DefaultRunningQuaterConsumptionRate
            elif currentSpeed < self.__maxSpeed * 0.5:
                consumption = config.DefaultRunningHalfConsumptionRate
            elif currentSpeed < self.__maxSpeed * 0.75:
                consumption = config.DefaultRunningHalfConsumptionRate
            elif currentSpeed < self.__maxSpeed:
                consumption = config.DefaultRunningUpperHalfConsumptionRate
            elif currentSpeed == config.DefaultMaxSpeed:
                consumption = config.DefaultRunningMaxSpeedConsumptionRate
        else:
            consumption = 0

        return consumption * self.__coefficient

    def IncreaseSpeedTo(self, speed: int):
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

        self.__engine.Consume(self.CalculateConsumptionRate)

    def ReduceSpeedBy(self, reduceBy: int):
        if not self.__engine.IsRunning:
            return

        self.__actualSpeed -= min(reduceBy, self.__brakingSpeed)

        if self.__actualSpeed < 0:
            self.__actualSpeed = 0

        self.__engine.Consume(self.CalculateConsumptionRate)
