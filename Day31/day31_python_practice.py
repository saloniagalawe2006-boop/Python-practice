"""
🐍 Day 31: Functions — Basics
"""

# ----------------------------------------------------
# 1. Defining and calling a simple function
# ----------------------------------------------------
# syntax: def function_name():
#             code block

def greet():
    print("Hello! Welcome to Day 31.")

greet()   # calling the function


# ----------------------------------------------------
# 2. Functions with parameters
# ----------------------------------------------------

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Rahul")
greet_user("Priya")


# ----------------------------------------------------
# 3. Functions with multiple parameters
# ----------------------------------------------------

def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)


# ----------------------------------------------------
# 4. Functions that RETURN a value
# ----------------------------------------------------

def multiply(a, b):
    return a * b

result = multiply(4, 6)
print("\nMultiply result:", result)


# ----------------------------------------------------
# 5. Default parameter values
# ----------------------------------------------------

def power(base, exponent=2):
    return base ** exponent

print("\npower(5):", power(5))          # uses default exponent=2
print("power(5, 3):", power(5, 3))      # overrides default


# ----------------------------------------------------
# 6. Keyword arguments (order doesn't matter)
# ----------------------------------------------------

def describe_student(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_student(name="Anjali", city="Mumbai", age=21)


# ----------------------------------------------------
# 7. Variable number of arguments (*args)
# ----------------------------------------------------

def total_sum(*numbers):
    return sum(numbers)

print("\nSum of 1,2,3:", total_sum(1, 2, 3))
print("Sum of 10,20,30,40:", total_sum(10, 20, 30, 40))


# ----------------------------------------------------
# 8. Variable number of keyword arguments (**kwargs)
# ----------------------------------------------------

def print_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\nUser profile:")
print_profile(name="Vikram", age=25, city="Delhi")


# ----------------------------------------------------
# 9. Real-world example: reusable calculator functions
# ----------------------------------------------------

def calculate_average(scores):
    return sum(scores) / len(scores)

def is_passing(average, passing_marks=50):
    return average >= passing_marks

student_scores = [90, 85, 88]
avg = calculate_average(student_scores)
print(f"\nAverage: {avg:.2f}")
print("Passing?", is_passing(avg))


"""
📝 Quick Recap:
- def function_name(params):  -> defines a function
- return value                 -> sends a value back to the caller
- Default params:  def f(a, b=10):
- Keyword args:     f(a=1, b=2)  -> order doesn't matter
- *args   -> collects extra positional args into a tuple
- **kwargs -> collects extra keyword args into a dict
- Functions make code reusable, organized, and easy to test
"""