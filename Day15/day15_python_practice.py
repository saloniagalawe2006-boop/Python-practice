# ============================================================
# Day 16 - f-strings Deep Dive
# File: day16_fstrings_deep_dive.py
# ============================================================


# ── SECTION 1: Expressions Inside f-strings ───────────────────

a = 10
b = 3

print(f"{a} + {b} = {a + b}")
# You can put ANY valid Python expression inside {} - not just a bare variable!

print(f"{a} squared is {a ** 2}")
print(f"Is {a} greater than {b}? {a > b}")
# Even comparisons (which return True/False) work directly inside {}


# ── SECTION 2: Calling Functions and Methods Inside {} ────────

name = "  rahul sharma  "

print(f"Cleaned name: {name.strip().title()}")
# Method chaining works DIRECTLY inside the f-string's curly braces

numbers = [12, 45, 7, 23, 56]
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")
print(f"Total numbers: {len(numbers)}")
print(f"Sum of all: {sum(numbers)}")
# Built-in functions also work directly inside {}


# ── SECTION 3: Ternary Expressions Inside f-strings ────────────

age = 16
print(f"Status: {'Minor' if age < 18 else 'Adult'}")
# The ternary expression from Day 6 works perfectly inside an f-string!

score = 85
print(f"Result: {'Pass' if score >= 40 else 'Fail'} (Score: {score})")


# ── SECTION 4: Nested Quotes Inside f-strings ──────────────────

# Since Python 3.12, you CAN reuse the same quote type inside {} -
# but for compatibility/clarity, mixing quote types is still the safest habit:

person = {"name": "Priya", "age": 25}    # a dictionary (full detail on Day 25)
print(f"Name: {person['name']}, Age: {person['age']}")
# Outer f-string uses double quotes " ", inner dictionary keys use single quotes '
# This avoids any quote conflicts


# ── SECTION 5: Dynamic Width and Precision ─────────────────────

value = 3.14159265

width = 15
precision = 3
print(f"[{value:{width}.{precision}f}]")
# The width and precision themselves come from VARIABLES, not hardcoded numbers!
# This is incredibly useful when formatting needs to adapt at runtime

for p in range(1, 6):
    print(f"Pi to {p} decimal places: {value:.{p}f}")
# Looping to show increasing precision, using the loop variable INSIDE the format spec


# ── SECTION 6: The = Debugging Specifier (Python 3.8+) ─────────

x = 25
y = 4

print(f"{x = }")             # Output: x = 25   (prints BOTH the expression text AND its value!)
print(f"{y = }")             # Output: y = 4
print(f"{x + y = }")         # Output: x + y = 29
print(f"{x * y = }")         # Output: x * y = 100
# This is EXTREMELY useful for quick debugging - no need to write f"x = {x}" manually!


# ── SECTION 7: Escaping Curly Braces ──────────────────────────

print(f"{{This looks like a placeholder but isn't}}")
# Double curly braces {{ }} -> Python prints a SINGLE literal { or }

value2 = 100
print(f"{{value2}} is literally shown, but {value2} shows the actual value")
# Compare: {{value2}} stays as text "{value2}", but {value2} shows 100


# ── SECTION 8: Multi-line f-strings ────────────────────────────

product = "Laptop"
price = 55000
quantity = 2

receipt = f"""
========================
       RECEIPT
========================
Product : {product}
Price   : Rs. {price:,}
Quantity: {quantity}
Total   : Rs. {price * quantity:,}
========================
"""
print(receipt)
# Triple quotes \"\"\" allow MULTI-LINE strings, and f-string formatting
# still works perfectly inside them, across multiple lines


# ── SECTION 9: Formatting Inside Loops — Practical Use ─────────

print("--- Formatted Score Report ---")
students_scores = [("Rahul", 78), ("Priya", 92), ("Anjali", 45), ("Vikram", 88)]

for student, marks in students_scores:
    status = "Pass" if marks >= 40 else "Fail"
    bar = "#" * (marks // 5)    # visual bar made of # characters, scaled down
    print(f"{student:<10}{marks:>5} | {bar:<20} {status}")


# ── SECTION 10: Practical — Live Calculation Display ───────────

print("\n--- Live Shopping Cart ---")
cart = [("Shirt", 799.0, 2), ("Jeans", 1499.0, 1), ("Socks", 99.0, 3)]

print(f"{'Item':<10}{'Price':>10}{'Qty':>6}{'Subtotal':>12}")
print("-" * 38)

cart_total = 0
for item, price_each, qty in cart:
    subtotal = price_each * qty
    cart_total += subtotal
    print(f"{item:<10}{price_each:>10.2f}{qty:>6}{subtotal:>12.2f}")

print("-" * 38)
print(f"{'Grand Total':<26}{cart_total:>12.2f}")


# ── SECTION 11: Practical — Temperature Converter with Debug Specifier ─

celsius = 37.5
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f"\n{celsius = }°C")
print(f"{fahrenheit = :.1f}°F")
print(f"{kelvin = :.2f}K")
# Notice: you CAN combine the = debug specifier WITH normal format specs too!

# ============================================================
# END OF DAY 16
# ============================================================