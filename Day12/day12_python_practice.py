# ============================================================
# Day 12 - Arguments & Return (Going Deeper)
# File: day12_arguments_and_return.py
# ============================================================


# ── SECTION 1: Recap — Positional Arguments (order matters) ──

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rocky")
# 1st argument "dog"   -> goes to 1st parameter 'animal'
# 2nd argument "Rocky" -> goes to 2nd parameter 'name'

describe_pet("Rocky", "dog")
# ⚠️ Still runs, but the MEANING is now wrong (logically incorrect, not a crash)
# Output: "I have a Rocky named dog." <- this is WRONG, order matters!


# ── SECTION 2: Keyword Arguments — naming which is which ─────

describe_pet(animal="cat", name="Whiskers")
# Now we EXPLICITLY tell Python which value goes to which parameter.
# Order no longer matters because we are naming them directly.

describe_pet(name="Tweety", animal="bird")
# Same result as above, just written in a different order -
# Python doesn't care about order when you use keyword arguments.


# ── SECTION 3: Mixing Positional and Keyword Arguments ────────

def order_pizza(size, topping, quantity):
    print(f"Order: {quantity} {size} pizza(s) with {topping}.")

order_pizza("Large", topping="Cheese", quantity=2)
# "Large" is positional (goes to 'size' by position - must come FIRST)
# topping= and quantity= are keyword - can be in any order AFTER the positional one

# RULE: Positional arguments must ALWAYS come BEFORE keyword arguments.
# order_pizza(topping="Cheese", "Large", quantity=2)  ← ❌ This would CRASH


# ── SECTION 4: Default Parameter Values (preview, detail on Day 14) ─

def greet_with_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_default("Rahul")               # uses the default "Hello"
greet_with_default("Priya", "Welcome")    # overrides the default


# ── SECTION 5: return vs print — Seeing the Difference Clearly ─

def add_and_print(a, b):
    print(a + b)            # just displays it - gives nothing back

def add_and_return(a, b):
    return a + b              # gives the value back - displays nothing

print("--- Using print-only function ---")
value1 = add_and_print(5, 3)     # this LINE prints "8" immediately (from inside the function)
print(f"What got stored: {value1}")   # but value1 is None! Nothing was returned.

print("\n--- Using return function ---")
value2 = add_and_return(5, 3)    # this line shows NOTHING by itself
print(f"What got stored: {value2}")   # value2 actually holds 8, because it was returned


# ── SECTION 6: return Exits the Function Immediately ─────────

def check_age(age):
    if age < 0:
        return "Invalid age! Cannot be negative."
    if age < 18:
        return "Minor"
    return "Adult"
    # Notice: as soon as ANY return runs, the function STOPS right there.
    # The remaining return lines are simply never reached for that call.

print("\n--- Early return demonstration ---")
print(check_age(-5))    # hits the FIRST return, never even looks at the rest
print(check_age(15))    # skips first return (false), hits SECOND return
print(check_age(25))    # skips first two, reaches the LAST return


# ── SECTION 7: Returning Multiple Values ──────────────────────

def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
    # This packages TWO values together and sends both back at once

rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"\nArea: {rect_area}, Perimeter: {rect_perimeter}")

# You can also grab the result WITHOUT immediately unpacking:
result = calculate_rectangle(5, 3)
print(result)            # prints as a pair: (15, 16)
print(type(result))      # <class 'tuple'> - more on this on Day 24


# ── SECTION 8: Functions with NO return — Always Give None ───

def show_message():
    print("This function only prints, never returns anything.")

captured = show_message()
print(f"\nCaptured value: {captured}")
print(f"Type of captured value: {type(captured)}")
# Output: None  and  <class 'NoneType'>
# This proves: NO return statement = the function ALWAYS gives back None


# ── SECTION 9: Practical — Validating Input Using Early Return ─

def validate_password(password):
    if len(password) < 8:
        return "Too short! Must be at least 8 characters."
    if password.isdigit():
        return "Too weak! Cannot be only numbers."
    if password.islower():
        return "Add at least one uppercase letter."
    return "Password looks strong!"

print("\n--- Password Validator ---")
print(validate_password("abc"))             # fails length check first
print(validate_password("12345678"))        # passes length, fails digit-only check
print(validate_password("password123"))     # passes those, fails uppercase check
print(validate_password("Password123"))     # passes everything


# ── SECTION 10: Practical — Function Returning Calculated Results ─

def split_bill(total_amount, number_of_people):
    if number_of_people <= 0:
        return None, "Error: Number of people must be at least 1."
    share = total_amount / number_of_people
    return round(share, 2), "Success"

print("\n--- Bill Splitter ---")
share_amount, status = split_bill(1500, 4)
print(f"Status: {status}, Each person pays: Rs. {share_amount}")

share_amount2, status2 = split_bill(1500, 0)
print(f"Status: {status2}, Each person pays: {share_amount2}")

# ============================================================
# END OF DAY 12
# ============================================================