"""
🐍 Day 52: Context Managers (the 'with' statement)
"""

# ----------------------------------------------------
# 1. You already know one context manager: file handling!
# ----------------------------------------------------

with open("demo.txt", "w") as file:
    file.write("Hello from Day 52!")
# file is AUTOMATICALLY closed here, even if an error happened above

print("File written and closed automatically.")


# ----------------------------------------------------
# 2. What is a Context Manager, really?
# ----------------------------------------------------
# It's an object that defines SETUP and CLEANUP behavior
# around a block of code, using two special methods:
#   __enter__  -> runs when entering the 'with' block
#   __exit__   -> runs when leaving the 'with' block (always!)


# ----------------------------------------------------
# 3. Creating a custom context manager (class-based)
# ----------------------------------------------------

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("Timer started...")
        return self          # this becomes the 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        end = time.time()
        print(f"Timer stopped. Elapsed: {end - self.start:.4f} seconds")
        return False          # False means: don't suppress any exception

print("\n--- Custom class-based context manager ---")
with Timer() as t:
    total = sum(range(1000000))
print("Sum result:", total)


# ----------------------------------------------------
# 4. __exit__ runs even if an error occurs inside the block
# ----------------------------------------------------

class SafeBlock:
    def __enter__(self):
        print("\nEntering safe block...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting safe block (cleanup always happens).")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True    # True means: SUPPRESS the exception (don't crash)

with SafeBlock():
    print("Doing risky work...")
    result = 10 / 0    # this would normally crash the program
print("Program continues normally after the block!")


# ----------------------------------------------------
# 5. Creating a context manager using @contextmanager (simpler way)
# ----------------------------------------------------

from contextlib import contextmanager

@contextmanager
def open_resource(name):
    print(f"\nOpening resource: {name}")
    yield name          # code before yield = __enter__, after yield = __exit__
    print(f"Closing resource: {name}")

with open_resource("Database Connection") as res:
    print(f"Using {res}...")


# ----------------------------------------------------
# 6. Real-world example: managing a "lock" during a task
# ----------------------------------------------------

@contextmanager
def task_lock(task_name):
    print(f"🔒 Locking: {task_name}")
    try:
        yield
    finally:
        print(f"🔓 Unlocking: {task_name}")

with task_lock("Update Inventory"):
    print("Performing inventory update...")


# ----------------------------------------------------
# 7. Multiple context managers in one 'with' statement
# ----------------------------------------------------

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content for file 1")
    f2.write("Content for file 2")

print("\nBoth files written and closed together.")


# ----------------------------------------------------
# 8. Cleanup demo files
# ----------------------------------------------------

import os
os.remove("demo.txt")
os.remove("file1.txt")
os.remove("file2.txt")
print("\nDemo files cleaned up.")


"""
📝 Quick Recap:
- 'with' statement handles SETUP and CLEANUP automatically
- Class-based: define __enter__(self) and __exit__(self, exc_type, exc_value, tb)
- __exit__ returning True SUPPRESSES exceptions; False lets them propagate
- @contextmanager decorator (from contextlib) is a simpler generator-based
  way to write context managers: code before yield = setup,
  after yield = cleanup
- Multiple resources: with open(a) as x, open(b) as y:
- Common uses: files, database connections, locks, timers, temp settings
"""