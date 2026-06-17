# ============================================================
# Day 06 - Conditions: if, elif, else
# File: day06_conditions.py
# ============================================================


# ── SECTION 1: Your First if Statement ───────────────────────

age = 20

if age >= 18:
    print("You are an adult.")

print("This line always runs.")


# ── SECTION 2: if-else ────────────────────────────────────────

age2 = 15

if age2 >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# ── SECTION 3: if-elif-else ──────────────────────────────────

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")


# ── SECTION 4: Multiple Conditions with and / or ─────────────

temperature = 35
is_raining  = False

if temperature > 30 and not is_raining:
    print("It's hot and dry. Drink water!")

if temperature > 30 or is_raining:
    print("Carry an umbrella or stay hydrated.")


# ── SECTION 5: Nested if (if inside if) ──────────────────────

username = "admin"
password = "1234"

if username == "admin":
    print("Username correct.")
    if password == "1234":
        print("Password correct. Access granted!")
    else:
        print("Wrong password. Access denied.")
else:
    print("Unknown username. Access denied.")


# ── SECTION 6: Checking Multiple Values (Membership) ─────────

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

# Cleaner way using 'in':
if day in ["Saturday", "Sunday"]:
    print("Weekend confirmed using 'in'.")


# ── SECTION 7: Ternary (One-Line if-else) ────────────────────

number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)
# This is a shortcut for:
# if number % 2 == 0:
#     result = "Even"
# else:
#     result = "Odd"


# ── SECTION 8: Practical — Login System ──────────────────────

print("\n--- Login System ---")
correct_username = "rahul"
correct_password = "python123"

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login successful! Welcome, " + entered_username + ".")
elif entered_username != correct_username:
    print("Username not found.")
else:
    print("Incorrect password.")


# ── SECTION 9: Practical — Grade Calculator ──────────────────

print("\n--- Grade Calculator ---")
student_marks = int(input("Enter your marks (0-100): "))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks entered!")
elif student_marks >= 90:
    print("Grade: A+ (Outstanding)")
elif student_marks >= 75:
    print("Grade: A (Excellent)")
elif student_marks >= 60:
    print("Grade: B (Good)")
elif student_marks >= 40:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail)")


# ── SECTION 10: Practical — Number Classifier ────────────────

print("\n--- Number Classifier ---")
num = int(input("Enter a number: "))

if num > 0:
    parity = "Even" if num % 2 == 0 else "Odd"
    print(f"{num} is Positive and {parity}.")
elif num < 0:
    parity = "Even" if num % 2 == 0 else "Odd"
    print(f"{num} is Negative and {parity}.")
else:
    print(f"{num} is Zero.")

# ============================================================
# END OF DAY 06
# ============================================================