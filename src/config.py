from os import stat


class config():
    @staticmethod
    def DefaultFillLevel():
        return 20

    @staticmethod
    def DefaultTankSize():
        return 60

    @staticmethod
    def DefaultOnReserveBorder():
        return 5

    @staticmethod
    def DefaultMaxAccelerationRatio():
        return 20

    @staticmethod
    def DefaultMinAccelerationRatio():
        return 5

    @staticmethod
    def DefaultMaxSpeed():
        return 250

    @staticmethod
    def DefaultBrakingSpeed():
        return 10

    @staticmethod
    def AccelerationRatio():
        return 10
