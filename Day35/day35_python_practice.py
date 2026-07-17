"""
🐍 Day 35: Modules & Import
"""

# ----------------------------------------------------
# 1. What is a Module?
# ----------------------------------------------------
# A module is simply a .py file containing code (functions,
# variables, classes) that you can REUSE in other files.
# Python also comes with many BUILT-IN modules ready to use.


# ----------------------------------------------------
# 2. Importing a built-in module
# ----------------------------------------------------

import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))


# ----------------------------------------------------
# 3. Importing specific functions using 'from ... import'
# ----------------------------------------------------

from math import sqrt, pow

print("\nsqrt(25):", sqrt(25))
print("pow(2, 5):", pow(2, 5))


# ----------------------------------------------------
# 4. Importing a module with an alias
# ----------------------------------------------------

import random as rnd

print("\nRandom number (1-10):", rnd.randint(1, 10))

fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit:", rnd.choice(fruits))

shuffled = fruits.copy()
rnd.shuffle(shuffled)
print("Shuffled list:", shuffled)


# ----------------------------------------------------
# 5. The 'datetime' module — dates and times
# ----------------------------------------------------

import datetime

now = datetime.datetime.now()
print("\nCurrent date & time:", now)
print("Current year:", now.year)


# ----------------------------------------------------
# 6. The 'os' module — interact with the operating system
# ----------------------------------------------------

import os

print("\nCurrent working directory:", os.getcwd())


# ----------------------------------------------------
# 7. Importing everything from a module (NOT recommended)
# ----------------------------------------------------
# from math import *   # avoid this -> pollutes namespace,
#                         can cause naming conflicts


# ----------------------------------------------------
# 8. Creating and importing YOUR OWN module
# ----------------------------------------------------
# Suppose you create a file called "my_utils.py" with:
#
#     def greet(name):
#         return f"Hello, {name}!"
#
#     PI = 3.14159
#
# Then in another file (same folder), you can do:
#
#     import my_utils
#     print(my_utils.greet("Rahul"))
#     print(my_utils.PI)
#
# This is exactly how large Python projects are organized —
# split code across multiple files and import what you need.


# ----------------------------------------------------
# 9. Checking what's inside a module
# ----------------------------------------------------

print("\nSome functions available in 'random' module:")
print([item for item in dir(rnd) if not item.startswith("_")][:10])


"""
📝 Quick Recap:
- import module_name              -> use as module_name.function()
- from module import func         -> use func() directly
- import module_name as alias     -> shorter name for convenience
- Built-in modules: math, random, datetime, os, sys, json, etc.
- You can create your OWN modules -> just save a .py file and import it
- Avoid 'from module import *' -> can cause naming conflicts
"""