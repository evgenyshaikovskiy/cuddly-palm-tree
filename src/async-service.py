import asyncio
from models.car import Car


async def main():
    # create default car modeling.
    car: Car = Car()

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
        action = int(input())

        match action:
            case 1:
                car.EngineStart()
                await asyncio.sleep(2)
                continue
            case 2:
                car.EngineStop()
                await asyncio.sleep(2)
                continue
            case 3:
                car.RunningIdle()
                await asyncio.sleep(3)
                continue
            case 4:
                car.FreeWheel()
                await asyncio.sleep(3)
                continue
            case 5:
                print('Input count of km/h to brake by')
                speed = int(input())
                car.BrakeBy(speed)
                await asyncio.sleep(3)
                continue
            case 6:
                print('Input count of km/h to accelerate by')
                speed = int(input())
                car.Accelerate(speed)
                await asyncio.sleep(3)
                continue
            case 7:
                print('Input amount of liters to refuel')
                liters = float(input())
                car.Refuel(liters)
                await asyncio.sleep(3)
                continue
            case 8:
                car.GetInformationOnCar()
                await asyncio.sleep(3)
                continue


asyncio.run(main())
