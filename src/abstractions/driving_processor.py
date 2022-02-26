from abc import ABCMeta, abstractclassmethod, abstractproperty


# class that represents 'proccesor' of vehicle
class AbstractDrivingProcessor():

    __metaclass__ = ABCMeta

    @abstractproperty
    def ActualSpeed():
        """Gets actual speed of vehicle.(int)"""

    @abstractclassmethod
    def IncreaseSpeedTo(speed: int):
        """Increase speed until certain 'speed' (in kilometrs per hour)"""

    @abstractclassmethod
    def ReduceSpeedTo(speed: int):
        """Reduces speed to certain value 'speed'(in kilometers per hour)"""
