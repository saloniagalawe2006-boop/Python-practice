"""
🐍 Day 45: Decorators
"""

# ----------------------------------------------------
# 1. Functions are objects -> can be passed around
# ----------------------------------------------------

def greet():
    return "Hello!"

def call_function(func):
    print("Calling the function passed in:", func())

call_function(greet)


# ----------------------------------------------------
# 2. A function can return another function
# ----------------------------------------------------

def outer():
    def inner():
        return "I'm the inner function!"
    return inner

my_func = outer()
print("\nCalling returned inner function:", my_func())


# ----------------------------------------------------
# 3. What is a Decorator?
# ----------------------------------------------------
# A decorator is a function that WRAPS another function,
# adding extra behavior WITHOUT changing its original code.

def my_decorator(func):
    def wrapper():
        print("Something happens BEFORE the function runs.")
        func()
        print("Something happens AFTER the function runs.")
    return wrapper

def say_hello():
    print("Hello, Day 45!")

decorated_hello = my_decorator(say_hello)   # manual decoration
print("\n--- Manual decoration ---")
decorated_hello()


# ----------------------------------------------------
# 4. Using the @ syntax (the real way decorators are used)
# ----------------------------------------------------

@my_decorator
def say_bye():
    print("Bye, see you tomorrow!")

print("\n--- Using @ syntax ---")
say_bye()   # same as: say_bye = my_decorator(say_bye)


# ----------------------------------------------------
# 5. Decorators for functions WITH arguments
# ----------------------------------------------------

def my_decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@my_decorator_with_args
def add(a, b):
    return a + b

print("\n--- Decorator with arguments ---")
add(3, 5)


# ----------------------------------------------------
# 6. Real-world example: timing a function's execution
# ----------------------------------------------------

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

print("\n--- Timing decorator ---")
slow_function()


# ----------------------------------------------------
# 7. Real-world example: login check decorator
# ----------------------------------------------------

def require_login(func):
    def wrapper(is_logged_in, *args, **kwargs):
        if not is_logged_in:
            print("Access denied! Please log in first.")
            return
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_dashboard():
    print("Welcome to your dashboard!")

print("\n--- Login check decorator ---")
view_dashboard(False)
view_dashboard(True)


# ----------------------------------------------------
# 8. Stacking multiple decorators
# ----------------------------------------------------

def bold(func):
    def wrapper():
        return f"**{func()}**"
    return wrapper

def italic(func):
    def wrapper():
        return f"_{func()}_"
    return wrapper

@bold
@italic
def text():
    return "Day 45"

print("\n--- Stacked decorators ---")
print(text())   # italic runs first, then bold wraps the result


"""
📝 Quick Recap:
- Functions can be passed as arguments and returned from other functions
- A decorator WRAPS a function to add extra behavior, without
  modifying its original code
- @decorator_name  above a function = shorthand for
  function = decorator_name(function)
- Use *args, **kwargs in the wrapper to support ANY function signature
- Common real-world uses: logging, timing, authentication checks,
  caching, access control
- Decorators can be stacked -> applied bottom-to-top
"""