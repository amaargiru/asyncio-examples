import asyncio
from datetime import datetime


async def periodic_fun1(a, b):
    while True:
        await asyncio.sleep(1)
        print(f"periodic_fun1 complete with result {a + b}")


async def periodic_fun2(a, b):
    while True:
        await asyncio.sleep(1)
        print(f"periodic_fun2 complete with result {a - b}")


async def main():
    start_time = datetime.now()

    asyncio.create_task(periodic_fun1(3, 2))
    asyncio.create_task(periodic_fun2(3, 2))

    await asyncio.sleep(10)

    duration_time = datetime.now() - start_time
    print(f"Total duration time: {duration_time}")


if __name__ == '__main__':
    asyncio.run(main())
