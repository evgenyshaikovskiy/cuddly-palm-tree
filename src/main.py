import asyncio
from abstractions.vehicle import AbstractVehicle
from utility.logger import Logger
from models.car import Car
from utility.restore import RestoreService
from utility.snapshot import SnapshotService


# consider to move to camel case convention naming
Logger.setup()
logger = Logger()


def main():
    # optional: add view on old session car params
    while(True):
        print('''Choose action:
              1 - Run new car.
              2 - Restore car from old session.
              3 - Destroy old session records.
              4 - Enable logging.
              5 - Disable logging.
              6 - Exit application.
              ''')

        action: int = int(input())
        if action == 1:
            asyncio.run(run_car(None))
        elif action == 2:
            restore_service: RestoreService = RestoreService()
            asyncio.run(run_car(restore_service.restore_car(logger)))
            print('restore service')
        elif action == 3:
            print('destroy service')
        elif action == 4:
            logger.enable_logging()
        elif action == 5:
            logger.disable_logging()
        elif action == 6:
            print('Closing application...')
            break


async def run_car(car: AbstractVehicle):
    if car is None:
        car = Car(logger)
    else:
        restore_service: RestoreService = RestoreService()
        car = restore_service.restore_car(logger)

    # start tracking new or already created car
    snapshot_service: SnapshotService = SnapshotService()
    car.subscribe(snapshot_service)
    while (True):
        print('''Choose action:
              1 - Start Engine.
              2 - Stop Engine.
              3 - Run Idle.
              4 - Free Wheel.
              5 - Brake by certain speed.
              6 - Accelerate by certain speed.
              7 - Refuel Car.
              8 - Get information about car condition.
              9 - To exit simulation.
              To cancel programm press Space.
              ''')
        action: int = int(input())

        if action == 1:
            car.engine_start()
            await asyncio.sleep(0.5)
        elif action == 2:
            car.engine_stop()
            await asyncio.sleep(0.5)
        elif action == 3:
            car.running_idle()
            await asyncio.sleep(0.5)
        elif action == 4:
            car.free_wheel()
            await asyncio.sleep(0.5)
            print('Input count of km/h to brake by')
        elif action == 5:
            speed = float(input())
            car.brake_by(speed)
            await asyncio.sleep(0.5)
        elif action == 6:
            print('Input count of km/h to accelerate by')
            speed = float(input())
            car.accelerate(speed)
            await asyncio.sleep(0.5)
        elif action == 7:
            print('Input amount of liters to refuel')
            liters = float(input())
            car.refuel(liters)
            await asyncio.sleep(0.5)
        elif action == 8:
            car.get_report_on_car()
            await asyncio.sleep(0.5)
        elif action == 9:
            print('Stopping simulation...')
            break

main()
