"""
🐍 Day 53: Threading & Multiprocessing (Basics)
"""

import threading
import multiprocessing
import time

# ----------------------------------------------------
# 1. Why concurrency?
# ----------------------------------------------------
# Normally, Python runs code line by line (one task at a time).
# Threading/Multiprocessing let you run MULTIPLE tasks
# "at the same time" -> useful for speeding up I/O-bound
# or CPU-bound work.


# ----------------------------------------------------
# 2. Running tasks the NORMAL (sequential) way
# ----------------------------------------------------

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)
    print(f"Task {name} finished")

print("--- Sequential execution ---")
start = time.time()
task("A", 1)
task("B", 1)
print(f"Total time: {time.time() - start:.2f} seconds\n")


# ----------------------------------------------------
# 3. Running tasks using THREADING (good for I/O-bound work)
# ----------------------------------------------------
# I/O-bound = waiting on files, network requests, sleep, etc.

print("--- Threaded execution ---")
start = time.time()

t1 = threading.Thread(target=task, args=("A", 1))
t2 = threading.Thread(target=task, args=("B", 1))

t1.start()   # starts running in the background
t2.start()

t1.join()    # wait for t1 to finish before continuing
t2.join()    # wait for t2 to finish before continuing

print(f"Total time: {time.time() - start:.2f} seconds\n")


# ----------------------------------------------------
# 4. Threads share memory -> need care with shared data
# ----------------------------------------------------

counter = 0
lock = threading.Lock()    # prevents two threads from changing counter at once

def increment():
    global counter
    for _ in range(100000):
        with lock:          # only ONE thread can be inside this block at a time
            counter += 1

print("--- Threads sharing memory safely (using a Lock) ---")
threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final counter value:", counter)   # should be exactly 400000


# ----------------------------------------------------
# 5. Multiprocessing -> good for CPU-bound work
# ----------------------------------------------------
# CPU-bound = heavy calculations that need real parallel CPU cores.
# Each process gets its OWN separate memory (no shared-memory issues).

def cpu_heavy_task(n):
    total = sum(i * i for i in range(n))
    print(f"Computed sum of squares up to {n}: {total}")

if __name__ == "__main__":
    print("\n--- Multiprocessing execution ---")
    start = time.time()

    p1 = multiprocessing.Process(target=cpu_heavy_task, args=(1000000,))
    p2 = multiprocessing.Process(target=cpu_heavy_task, args=(1000000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Total time: {time.time() - start:.2f} seconds")


# ----------------------------------------------------
# 6. Threading vs Multiprocessing — when to use which
# ----------------------------------------------------
# THREADING:
#   - Best for I/O-bound tasks (file/network/database waiting)
#   - Lightweight, shares memory
#   - Limited by Python's GIL for CPU-heavy tasks
#
# MULTIPROCESSING:
#   - Best for CPU-bound tasks (heavy computation)
#   - True parallelism across CPU cores
#   - Higher memory overhead (separate memory per process)


"""
📝 Quick Recap:
- threading.Thread(target=func, args=(...)) -> creates a thread
- .start() begins execution, .join() waits for it to finish
- Use threading.Lock() to protect shared data from race conditions
- multiprocessing.Process(target=func, args=(...)) -> creates a process
- Threads = great for I/O-bound (waiting) tasks
- Processes = great for CPU-bound (heavy computation) tasks
- Always guard multiprocessing code with: if __name__ == "__main__":
"""