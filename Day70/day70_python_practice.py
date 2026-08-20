"""
🐍 Day 67: Async Programming — async / await (asyncio)
"""

import asyncio
import time

# ----------------------------------------------------
# 1. Why async? (recap: threading vs asyncio)
# ----------------------------------------------------
# asyncio runs many I/O-bound tasks CONCURRENTLY on a SINGLE thread
# by pausing/resuming tasks while they wait (e.g. network calls,
# sleep, file I/O) — no need for actual OS threads.


# ----------------------------------------------------
# 2. Defining an async function (a "coroutine")
# ----------------------------------------------------

async def say_hello():
    print("Hello,")
    await asyncio.sleep(1)     # pauses HERE, letting other tasks run
    print("Day 67!")

# You can't just call say_hello() like a normal function —
# it must be awaited or run inside an event loop.
asyncio.run(say_hello())


# ----------------------------------------------------
# 3. Sequential (blocking) vs Concurrent async execution
# ----------------------------------------------------

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")

async def run_sequential():
    print("\n--- Sequential async (await one at a time) ---")
    start = time.time()
    await task("A", 1)
    await task("B", 1)
    print(f"Total time: {time.time() - start:.2f} seconds")

asyncio.run(run_sequential())


async def run_concurrent():
    print("\n--- Concurrent async (asyncio.gather) ---")
    start = time.time()
    await asyncio.gather(
        task("A", 1),
        task("B", 1)
    )
    print(f"Total time: {time.time() - start:.2f} seconds")

asyncio.run(run_concurrent())


# ----------------------------------------------------
# 4. Creating tasks explicitly (runs in the background)
# ----------------------------------------------------

async def run_with_create_task():
    print("\n--- Using asyncio.create_task() ---")
    t1 = asyncio.create_task(task("X", 2))
    t2 = asyncio.create_task(task("Y", 1))

    print("Both tasks scheduled, doing other work...")
    await asyncio.sleep(0.5)
    print("Other work done, now waiting for tasks to finish...")

    await t1
    await t2

asyncio.run(run_with_create_task())


# ----------------------------------------------------
# 5. Real-world example: simulating multiple API calls
# ----------------------------------------------------

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)     # simulates network wait time
    return f"Data from {source}"

async def fetch_all_sources():
    print("\n--- Simulated concurrent API calls ---")
    start = time.time()

    results = await asyncio.gather(
        fetch_data("API-1", 1.5),
        fetch_data("API-2", 1.0),
        fetch_data("API-3", 0.5),
    )

    print("Results:", results)
    print(f"Total time: {time.time() - start:.2f} seconds (NOT 3.0!)")

asyncio.run(fetch_all_sources())


# ----------------------------------------------------
# 6. async for with an async generator
# ----------------------------------------------------

async def async_counter(limit):
    n = 1
    while n <= limit:
        await asyncio.sleep(0.2)
        yield n
        n += 1

async def use_async_generator():
    print("\n--- async generator with 'async for' ---")
    async for number in async_counter(5):
        print("Got:", number)

asyncio.run(use_async_generator())


"""
📝 Quick Recap:
- async def func(): -> defines a coroutine (an async function)
- await expression   -> pauses here until the awaited task completes
- asyncio.run(coro())  -> runs a coroutine as the program's entry point
- asyncio.sleep(sec)   -> non-blocking sleep (lets other tasks run)
- asyncio.gather(a, b) -> runs multiple coroutines CONCURRENTLY
- asyncio.create_task()-> schedules a coroutine to run in the background
- async for / async generators -> yield values asynchronously
- Best for I/O-bound work: API calls, file/network I/O, web servers
- NOT for CPU-heavy work -> use multiprocessing for that instead
"""