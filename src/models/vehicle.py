from abc import ABCMeta, abstractclassmethod, abstractproperty


# Abstact class that describes vehicles
class AbstractVehicle():
    __metaclass__ = ABCMeta

    @abstractproperty
    def EngineIsRunning():
        """Indicates whether engine is running or not"""

    @abstractclassmethod
    def EngineStart():
        """Starts an engine"""

    @abstractclassmethod
    def EngineStop():
        """Stops an engine"""

    @abstractclassmethod
    def Refuel(liters: float):
        """Refuel vehicle by certain amount of fuel(in liters)"""

    @abstractclassmethod
    def RunningIdle():
        """Method which runs vehicle until certain event"""

    @abstractclassmethod
    def FreeWheel():
        """Method which runs vehicle in mode where fuel doesn't consume"""

    @abstractclassmethod
    def BrakeBy(speed: int):
        """Method which launches breaking in vehicle"""

    @abstractclassmethod
    def Accelerate(speed: int):
        """Method which launches acceleration in vehicle"""
