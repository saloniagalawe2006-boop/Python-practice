"""
🐍 Day 63: String Formatting — f-strings, format(), % (Deep Dive)
"""

# ----------------------------------------------------
# 1. The three main ways to format strings in Python
# ----------------------------------------------------

name = "Rahul"
age = 22
gpa = 8.6789

# Old style (%)
old_style = "Name: %s, Age: %d" % (name, age)

# .format() method
format_method = "Name: {}, Age: {}".format(name, age)

# f-strings (modern, preferred way)
f_string = f"Name: {name}, Age: {age}"

print(old_style)
print(format_method)
print(f_string)


# ----------------------------------------------------
# 2. f-strings can hold any expression, not just variables
# ----------------------------------------------------

a, b = 5, 3
print(f"\n{a} + {b} = {a + b}")
print(f"Uppercase name: {name.upper()}")
print(f"Is age >= 18? {age >= 18}")


# ----------------------------------------------------
# 3. Controlling decimal places
# ----------------------------------------------------

print(f"\nGPA rounded to 2 decimals: {gpa:.2f}")
print(f"GPA rounded to 1 decimal: {gpa:.1f}")
print(f"GPA as percentage: {gpa/10:.1%}")


# ----------------------------------------------------
# 4. Padding and alignment
# ----------------------------------------------------

print("\n--- Alignment ---")
print(f"[{name:<10}]")   # left align, width 10
print(f"[{name:>10}]")   # right align, width 10
print(f"[{name:^10}]")   # center align, width 10
print(f"[{name:*^10}]")  # center align, padded with *


# ----------------------------------------------------
# 5. Number formatting -> commas, leading zeros, signs
# ----------------------------------------------------

big_number = 1234567
print("\n--- Number formatting ---")
print(f"With commas: {big_number:,}")
print(f"With leading zeros: {42:05d}")
print(f"With + sign: {42:+d}")
print(f"Negative with sign: {-42:+d}")


# ----------------------------------------------------
# 6. Formatting in different number bases
# ----------------------------------------------------

num = 255
print("\n--- Number bases ---")
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hexadecimal: {num:x}")
print(f"Hex (uppercase): {num:X}")


# ----------------------------------------------------
# 7. Using = for quick debugging (Python 3.8+)
# ----------------------------------------------------

x = 10
y = 25
print(f"\n{x=}")
print(f"{y=}")
print(f"{x + y=}")


# ----------------------------------------------------
# 8. Multi-line f-strings and nested formatting
# ----------------------------------------------------

price = 499.5
quantity = 3
total = price * quantity

receipt = f"""
--- Receipt ---
Item price: ${price:.2f}
Quantity: {quantity}
Total: ${total:.2f}
"""
print(receipt)


# ----------------------------------------------------
# 9. Real-world example: formatted table output
# ----------------------------------------------------

students = [("Rahul", 90.456), ("Priya", 85.123), ("Anjali", 95.789)]

print("--- Student Report ---")
print(f"{'Name':<10}{'Score':>10}")
print("-" * 20)
for student_name, score in students:
    print(f"{student_name:<10}{score:>10.2f}")


"""
📝 Quick Recap:
- f"{variable}"          -> modern, preferred way (f-string)
- f"{expr:.2f}"          -> 2 decimal places
- f"{val:<10} / >10 / ^10" -> left / right / center align, width 10
- f"{num:,}"             -> thousands separator
- f"{num:05d}"           -> pad with leading zeros
- f"{num:+d}"            -> always show sign
- f"{num:b} / :o / :x"   -> binary / octal / hex
- f"{var=}"              -> quick debug print (shows name AND value)
- f-strings are faster and more readable than % or .format()
"""