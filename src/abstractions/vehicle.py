from abc import ABC, abstractmethod


# Abstact class that describes vehicles
class AbstractVehicle(ABC):

    @property
    @abstractmethod
    def EngineIsRunning(self):
        """Indicates whether engine is running or not"""

    @abstractmethod
    def EngineStart(self):
        """Starts an engine"""

    @abstractmethod
    def EngineStop(self):
        """Stops an engine"""

    @abstractmethod
    def Refuel(self, liters: float):
        """Refuel vehicle by certain amount of fuel(in liters)"""

    @abstractmethod
    def RunningIdle(self):
        """Method which runs vehicle until certain event"""

    @abstractmethod
    def FreeWheel(self):
        """Method which runs vehicle in mode where fuel doesn't consume"""

    @abstractmethod
    def BrakeBy(self, speed: float):
        """Method which launches breaking in vehicle"""

    @abstractmethod
    def Accelerate(self, speed: float):
        """Method which launches acceleration in vehicle"""
