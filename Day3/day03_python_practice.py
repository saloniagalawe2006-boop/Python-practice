# ============================================================
# Day 03 - User Input & type()
# File: day03_user_input.py
# ============================================================


# ── SECTION 1: Your First input() ────────────────────────────

name = input("What is your name? ")

print("Hello,", name)


# ── SECTION 2: type() — What kind of data is this? ───────────

age_input = input("Enter your age: ")

print(type(age_input))


# ── SECTION 3: The Big Problem — input() gives STRING always ──

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print(num1 + num2)


# ── SECTION 4: The Fix — Convert string to int ───────────────

num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))

print(num3 + num4)


# ── SECTION 5: Converting to float ───────────────────────────

price = float(input("Enter the price: "))

print("Price entered:", price)
print("With 18% GST:", price + (price * 18 / 100))


# ── SECTION 6: type() on all data types ──────────────────────

whole_number   = 100
decimal_number = 3.14
some_text      = "Python"
true_or_false  = True

print(type(whole_number))
print(type(decimal_number))
print(type(some_text))
print(type(true_or_false))


# ── SECTION 7: Checking types with isinstance() ───────────────

my_value = 42

print(isinstance(my_value, int))
print(isinstance(my_value, str))
print(isinstance(my_value, float))


# ── SECTION 8: Full Interactive Profile ──────────────────────

print("==================================")
print("     TELL ME ABOUT YOURSELF")
print("==================================")

user_name = input("Your name    : ")
user_age  = int(input("Your age     : "))
user_city = input("Your city    : ")

print()
print("==================================")
print("         YOUR PROFILE")
print("==================================")
print(f"  Name : {user_name}")
print(f"  Age  : {user_age}")
print(f"  City : {user_city}")
print(f"  In 5 years you will be {user_age + 5} years old.")
print("==================================")

# ============================================================
# END OF DAY 03
# ============================================================