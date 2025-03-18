import asyncio


async def task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished after {seconds} seconds.")
    await asyncio.sleep(2)
    print(f"{name} finished")

async def main():
    await asyncio.gather(task("Task 1", 2), task("Task 2", 3))
    # asyncio.

asyncio.run(main())
