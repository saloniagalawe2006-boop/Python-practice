"""
🐍 Day 68: The functools Module
lru_cache, partial, wraps, reduce, total_ordering
"""

import functools
import time

# ----------------------------------------------------
# 1. functools.reduce() -> recap from Day 49
# ----------------------------------------------------

numbers = [1, 2, 3, 4, 5]
total = functools.reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", total)


# ----------------------------------------------------
# 2. functools.lru_cache() -> automatic memoization (caching)
# ----------------------------------------------------
# Speeds up expensive/repeated function calls by CACHING results.

@functools.lru_cache(maxsize=None)
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print("\n--- lru_cache speeding up recursion ---")
start = time.time()
result = slow_fibonacci(30)
print(f"fibonacci(30) = {result}, took {time.time() - start:.6f} sec (cached)")

print("Cache info:", slow_fibonacci.cache_info())


# ----------------------------------------------------
# 3. Comparing WITHOUT lru_cache (much slower for big n)
# ----------------------------------------------------

def plain_fibonacci(n):
    if n <= 1:
        return n
    return plain_fibonacci(n - 1) + plain_fibonacci(n - 2)

print("\n--- Without lru_cache ---")
start = time.time()
plain_fibonacci(28)
print(f"Plain fibonacci(28) took {time.time() - start:.4f} sec")


# ----------------------------------------------------
# 4. functools.partial() -> pre-fill some function arguments
# ----------------------------------------------------

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)     # exponent is FIXED to 2
cube = functools.partial(power, exponent=3)

print("\n--- functools.partial() ---")
print("square(5):", square(5))
print("cube(2):", cube(2))


# ----------------------------------------------------
# 5. functools.wraps() -> preserves function metadata in decorators
# ----------------------------------------------------
# Without @wraps, a decorated function LOSES its original
# name/docstring (they get replaced by the wrapper's).

def my_decorator(func):
    @functools.wraps(func)      # keeps the original name/docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print("\n--- functools.wraps() ---")
print(greet("Rahul"))
print("Function name:", greet.__name__)      # stays 'greet', not 'wrapper'
print("Docstring:", greet.__doc__)


# ----------------------------------------------------
# 6. functools.total_ordering -> auto-generate comparison methods
# ----------------------------------------------------
# Define __eq__ and ONE other (__lt__), get <=, >, >= for free!

@functools.total_ordering
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return f"{self.name}({self.score})"

s1 = Student("Rahul", 90)
s2 = Student("Priya", 85)

print("\n--- total_ordering ---")
print("s1 > s2:", s1 > s2)     # auto-generated from __lt__ and __eq__
print("s1 >= s2:", s1 >= s2)
print("s1 <= s2:", s1 <= s2)
print("Sorted:", sorted([s1, s2]))


# ----------------------------------------------------
# 7. Real-world example: caching an expensive database-like lookup
# ----------------------------------------------------

@functools.lru_cache(maxsize=100)
def get_user_data(user_id):
    print(f"  (Simulating slow lookup for user {user_id}...)")
    time.sleep(0.5)          # simulate a slow operation
    return f"User-{user_id}-Data"

print("\n--- Caching a slow lookup ---")
print(get_user_data(1))    # slow (not cached yet)
print(get_user_data(1))    # instant (cached!)
print(get_user_data(2))    # slow (new value)


"""
📝 Quick Recap:
- import functools
- reduce(func, iterable)      -> combine all items into one value
- @lru_cache(maxsize=...)     -> caches results, speeds up repeated calls
- partial(func, arg=value)    -> pre-fills arguments for a new function
- @wraps(func)                -> preserves name/docstring in decorators
- @total_ordering              -> auto-generates <=, >, >= from
  __eq__ + one comparison method (__lt__)
- Great for performance optimization (caching) and cleaner decorators
"""