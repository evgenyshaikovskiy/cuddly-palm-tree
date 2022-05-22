import click
from click_shell import shell

from abstractions.vehicle import AbstractVehicle
from utility.logger import Logger
from models.car import Car
from utility.restore import RestoreService
from utility.snapshot import SnapshotService


@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--disable-console',
    default=False,
    help="Set parameter as 'True' to disable console logging, otherwise 'False'."
)
@click.option(
    '--disable-file',
    default=False,
    help="Set this parameter as 'True' to disable file logging, otherwise 'False'."
)
@shell(prompt='> ', intro='Launching cli application...')
def main(use_save, disable_console, disable_file):
    Logger.setup()
    global restore_service
    global snapshot_service
    global car
    restore_service = RestoreService()
    snapshot_service = SnapshotService()
    car = None

    logger = Logger(disable_console, disable_file)

    if use_save:
        car = restore_service.restore_car(logger)

    if car is None:
        car = Car(logger)

    car.subscribe(snapshot_service)


@main.command(help='Starts car engine.', name='start-engine')
def start_engine():
    car.engine_start()


@main.command(help='Stops car engine.', name='stop-engine')
def stop_engine():
    car.engine_stop()


@main.command(help='Runs car in free wheel mode.', name='free-wheel')
def free_wheel():
    car.free_wheel()


@main.command(help='Runs car in idle mode.', name='run-idle')
def run_idle():
    car.running_idle()


@main.command(help='Prints available information on car.', name='info')
def info():
    car.get_report_on_car()


@main.command(help='Refuels car by given amount of liters', name='refuel')
@click.argument('liters')
def refuel(liters):
    try:
        liters = float(liters)
    except ValueError:
        print('Error! Given amount of liters is not correct.')
        return

    car.refuel(liters)


@main.command(help='Accelerate car by given amount of km/h', name='accelerate')
@click.argument('speed')
def accelerate(speed):
    try:
        speed = int(speed)
    except ValueError:
        print('Error! Given speed accelerate to is not correct.')
        return

    car.accelerate(speed)


@main.command(help='Brake car by given amount of km/h', name='brake')
@click.argument('speed')
def brake(speed):
    try:
        speed = int(speed)
    except ValueError:
        print('Error! Given speed to brake by is not correct.')
        return

    car.brake_by(speed)


if __name__ == '__main__':
    main()
