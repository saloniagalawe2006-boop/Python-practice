"""
🐍 Day 36: Error Handling — try / except
"""

# ----------------------------------------------------
# 1. Why error handling?
# ----------------------------------------------------
# Without handling, an error CRASHES the entire program.
# try/except lets you catch errors and keep running.

print("--- Without handling (would crash) ---")
# print(10 / 0)   # uncommenting this line would stop the whole program


# ----------------------------------------------------
# 2. Basic try / except
# ----------------------------------------------------

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# ----------------------------------------------------
# 3. Catching a specific exception with details
# ----------------------------------------------------

try:
    num = int("hello")
except ValueError as e:
    print("\nValueError caught:", e)


# ----------------------------------------------------
# 4. Handling MULTIPLE exception types
# ----------------------------------------------------

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Both values must be numbers!")

print("\n--- Multiple exceptions ---")
print(safe_divide(10, 2))
safe_divide(10, 0)
safe_divide(10, "two")


# ----------------------------------------------------
# 5. else -> runs ONLY if no exception occurred
# ----------------------------------------------------

print("\n--- try / except / else ---")
try:
    value = int("42")
except ValueError:
    print("Conversion failed!")
else:
    print("Conversion succeeded! Value:", value)


# ----------------------------------------------------
# 6. finally -> ALWAYS runs, error or not
# ----------------------------------------------------

print("\n--- try / except / finally ---")
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error!")
finally:
    print("This always runs (cleanup code goes here).")


# ----------------------------------------------------
# 7. Catching ANY exception (generic)
# ----------------------------------------------------

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except Exception as e:
    print("\nSomething went wrong:", e)


# ----------------------------------------------------
# 8. Raising your own errors
# ----------------------------------------------------

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

print("\n--- Custom raised error ---")
try:
    check_age(-5)
except ValueError as e:
    print("Caught custom error:", e)


# ----------------------------------------------------
# 9. Real-world example: safe user input handling
# ----------------------------------------------------

def get_valid_number(text):
    try:
        return float(text)
    except ValueError:
        print(f"'{text}' is not a valid number. Using 0 instead.")
        return 0

print("\n--- Safe input parsing ---")
print(get_valid_number("42.5"))
print(get_valid_number("abc"))


"""
📝 Quick Recap:
- try:      code that might fail
- except:   runs if an error occurs (can target specific error types)
- else:     runs ONLY if no error occurred
- finally:  ALWAYS runs (cleanup, closing files, etc.)
- raise:    manually trigger your own error
- Common exceptions: ZeroDivisionError, ValueError, TypeError,
  IndexError, KeyError, FileNotFoundError
- Error handling keeps programs running smoothly instead of crashing
"""