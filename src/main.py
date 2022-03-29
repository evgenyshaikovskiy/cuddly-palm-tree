import asyncio
from logger import logger
from models.car import Car

logger.setup()


async def main():
    # create default car modeling.
    logger_class = logger()
    logger_class.disable_logging()
    car: Car = Car(logger_class)

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
              To cancel programm press Space.
              ''')
        action: int = int(input())

        if action == 1:
            car.EngineStart()
            await asyncio.sleep(2)
        elif action == 2:
            car.EngineStop()
            await asyncio.sleep(2)
        elif action == 3:
            car.RunningIdle()
            await asyncio.sleep(3)
        elif action == 4:
            car.FreeWheel()
            await asyncio.sleep(3)
            print('Input count of km/h to brake by')
        elif action == 5:
            speed = int(input())
            car.BrakeBy(speed)
            await asyncio.sleep(3)
        elif action == 6:
            print('Input count of km/h to accelerate by')
            speed = int(input())
            car.Accelerate(speed)
            await asyncio.sleep(3)
        elif action == 7:
            print('Input amount of liters to refuel')
            liters = float(input())
            car.Refuel(liters)
            await asyncio.sleep(3)
        elif action == 8:
            car.GetInformationOnCar()
            await asyncio.sleep(3)


asyncio.run(main())
