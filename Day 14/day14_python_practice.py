# ============================================================
# Day 15 - String Formatting
# File: day15_string_formatting.py
# ============================================================


# ── SECTION 1: f-string Recap ─────────────────────────────────

name = "Rahul"
age = 22

print(f"My name is {name} and I am {age} years old.")
# Basic recap from Day 2 - variables inside {} get replaced with their values


# ── SECTION 2: Controlling Decimal Places ─────────────────────

price = 499.98765

print(f"{price}")          # Full precision, no formatting
print(f"{price:.2f}")      # 2 decimal places -> 499.99 (rounds!)
print(f"{price:.0f}")      # 0 decimal places -> 500 (rounded to whole number)
print(f"{price:.4f}")      # 4 decimal places -> 499.9877

pi = 3.14159265358979
print(f"Pi rounded to 2 places: {pi:.2f}")
print(f"Pi rounded to 5 places: {pi:.5f}")


# ── SECTION 3: Width and Alignment ────────────────────────────

word = "Hi"

print(f"[{word:10}]")      # Left-aligned by default (for strings), width 10
print(f"[{word:>10}]")     # Right-aligned, width 10
print(f"[{word:^10}]")     # Center-aligned, width 10
print(f"[{word:*^10}]")    # Center-aligned, padded with * instead of spaces

number = 42
print(f"[{number:10}]")    # Right-aligned by default (for numbers!)
print(f"[{number:<10}]")   # Left-aligned, width 10
print(f"[{number:^10}]")   # Center-aligned, width 10


# ── SECTION 4: Leading Zeros (Zero-Padding) ───────────────────

invoice_number = 7
print(f"Invoice No: {invoice_number:04}")    # 0007 - pads with zeros to width 4
print(f"Invoice No: {invoice_number:06}")    # 000007 - width 6

score = 95
print(f"Score: {score:03}")                  # 095


# ── SECTION 5: Adding Commas to Large Numbers ─────────────────

big_number = 1234567
print(f"{big_number:,}")          # 1,234,567 - comma every 3 digits

salary = 85000.5
print(f"Salary: Rs. {salary:,.2f}")  # combine comma AND 2 decimal places


# ── SECTION 6: Percentage Formatting ──────────────────────────

ratio = 0.856
print(f"{ratio:%}")            # 85.600000%  (multiplies by 100, adds %)
print(f"{ratio:.1%}")          # 85.6%  (1 decimal place)
print(f"{ratio:.2%}")          # 85.60%


# ── SECTION 7: Sign Display (+ / -) ───────────────────────────

profit = 5000
loss = -2000

print(f"{profit:+}")     # +5000  -> always show the sign
print(f"{loss:+}")       # -2000
print(f"{profit:+,}")     # +5,000  -> combine sign with comma formatting


# ── SECTION 8: Combining Multiple Format Specs ────────────────

product_price = 1234.5

print(f"[{product_price:>15,.2f}]")
# Right-aligned, width 15, comma separator, 2 decimal places - ALL together!


# ── SECTION 9: The .format() Method (Older Style) ─────────────

print("My name is {} and I am {} years old.".format(name, age))
# {} are placeholders, filled IN ORDER by .format()'s arguments

print("My name is {0} and I am {1} years old. {0} loves Python!".format(name, age))
# Numbers inside {} let you REUSE or REORDER arguments

print("{n} is {a} years old.".format(n=name, a=age))
# Named placeholders work too - similar to keyword arguments


# ── SECTION 10: The % Operator (Old Style, Recognize It) ───────

print("My name is %s and I am %d years old." % (name, age))
# %s = string placeholder, %d = integer placeholder
# This is rarely used in modern Python, but you'll see it in older codebases


# ── SECTION 11: Practical — Formatted Receipt ─────────────────

print("\n" + "=" * 40)
print("           STORE RECEIPT")
print("=" * 40)

items = [
    ("Apple",   3,  40.00),
    ("Bread",   2,  35.50),
    ("Milk",    1,  60.00),
]

grand_total = 0
for item_name, qty, unit_price in items:
    line_total = qty * unit_price
    grand_total += line_total
    print(f"{item_name:<10}{qty:>3} x {unit_price:>7.2f} = {line_total:>8.2f}")

print("-" * 40)
print(f"{'TOTAL':<10}{'':>3}   {'':>7} = {grand_total:>8.2f}")
print("=" * 40)


# ── SECTION 12: Practical — Student Marks Table ───────────────

print("\n" + "=" * 45)
print("            STUDENT MARK SHEET")
print("=" * 45)
print(f"{'Name':<12}{'Marks':>8}{'Percentage':>15}")
print("-" * 45)

students = [
    ("Rahul",   78, 100),
    ("Priya",   92, 100),
    ("Anjali",  45, 100),
]

for student_name, marks, total in students:
    percentage = (marks / total) * 100
    print(f"{student_name:<12}{marks:>8}{percentage:>14.1f}%")

print("=" * 45)

# ============================================================
# END OF DAY 15
# ============================================================