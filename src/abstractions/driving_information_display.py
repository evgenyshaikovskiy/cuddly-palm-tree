from abc import ABCMeta, abstractproperty


# class that describes actual information on vehicle speed and other parameters
class AbstractDrivingInformationDisplay():

    __metaclass__ = ABCMeta

    @abstractproperty
    def ActualSpeed():
        """Indicates actual speed of vehicle."""
