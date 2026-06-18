# ============================================================
# Day 07 - Nested Conditions
# File: day07_nested_conditions.py
# ============================================================


# ── SECTION 1: Basic Nested if ───────────────────────────────

age = 25

if age >= 18:
    print("You are eligible to apply.")
    if age >= 60:
        print("You qualify for senior citizen benefits too.")
    else:
        print("You are in the regular adult category.")
else:
    print("You are not eligible. Must be 18+.")


# ── SECTION 2: Three-Level Nesting — Driving License Check ───

driving_age   = 20
passed_test   = True
has_valid_id  = True

print("\n--- Driving License Application ---")

if driving_age >= 18:
    print("Step 1 passed: Age requirement met.")
    if passed_test:
        print("Step 2 passed: Driving test cleared.")
        if has_valid_id:
            print("Step 3 passed: Valid ID provided.")
            print("RESULT: License APPROVED!")
        else:
            print("RESULT: License REJECTED - No valid ID.")
    else:
        print("RESULT: License REJECTED - Failed driving test.")
else:
    print("RESULT: License REJECTED - Must be 18 or older.")


# ── SECTION 3: Nested if with elif inside ────────────────────

print("\n--- Movie Ticket Pricing ---")
age2     = 16
is_member = True

if age2 < 18:
    print("Category: Child/Teen")
    if is_member:
        print("Price: Rs. 100 (Member discount)")
    else:
        print("Price: Rs. 150 (Regular)")
elif age2 < 60:
    print("Category: Adult")
    if is_member:
        print("Price: Rs. 150 (Member discount)")
    else:
        print("Price: Rs. 200 (Regular)")
else:
    print("Category: Senior")
    if is_member:
        print("Price: Rs. 80 (Member discount)")
    else:
        print("Price: Rs. 100 (Regular)")


# ── SECTION 4: Comparing Nested if vs Combined 'and' ─────────

username = "rahul"
password = "py123"
is_active = True

print("\n--- Method A: Using Nested if (specific error messages) ---")
if username == "rahul":
    if password == "py123":
        if is_active:
            print("Login successful!")
        else:
            print("Account is deactivated. Contact support.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

print("\n--- Method B: Using 'and' (single combined check) ---")
if username == "rahul" and password == "py123" and is_active:
    print("Login successful!")
else:
    print("Login failed. Check your credentials.")
# Notice: Method B cannot tell you WHICH part failed — just a generic message.
# Method A can tell you EXACTLY what went wrong. Both are valid - choose based on need.


# ── SECTION 5: Nested Conditions for Number Classification ───

print("\n--- Advanced Number Classifier ---")
num = -14

if num >= 0:
    print(f"{num} is non-negative.")
    if num == 0:
        print("It is exactly Zero.")
    else:
        if num % 2 == 0:
            print("It is Positive and Even.")
        else:
            print("It is Positive and Odd.")
else:
    print(f"{num} is Negative.")
    if num % 2 == 0:
        print("It is Negative and Even.")
    else:
        print("It is Negative and Odd.")


# ── SECTION 6: Real World — Loan Eligibility Checker ─────────

print("\n--- Loan Eligibility Checker ---")
salary       = 45000
credit_score = 720
has_job      = True

if has_job:
    print("Employment check: PASSED")
    if salary >= 30000:
        print("Salary check: PASSED")
        if credit_score >= 700:
            print("Credit score check: PASSED")
            print("\nRESULT: LOAN APPROVED for up to Rs. 5,00,000")
        elif credit_score >= 600:
            print("Credit score check: PASSED (moderate)")
            print("\nRESULT: LOAN APPROVED for up to Rs. 2,00,000")
        else:
            print("Credit score check: FAILED")
            print("\nRESULT: LOAN REJECTED - Low credit score.")
    else:
        print("Salary check: FAILED")
        print("\nRESULT: LOAN REJECTED - Insufficient salary.")
else:
    print("Employment check: FAILED")
    print("\nRESULT: LOAN REJECTED - No active employment.")


# ── SECTION 7: Interactive — Restaurant Discount System ──────

print("\n--- Restaurant Bill Discount System ---")
bill_amount = float(input("Enter your bill amount: Rs. "))
is_weekend  = input("Is it a weekend? (yes/no): ").strip().lower() == "yes"

if bill_amount >= 1000:
    print("You qualify for the high-spender discount tier.")
    if is_weekend:
        discount = bill_amount * 0.20
        print("Weekend bonus discount applied: 20%")
    else:
        discount = bill_amount * 0.15
        print("Weekday discount applied: 15%")
else:
    print("You qualify for the standard discount tier.")
    if is_weekend:
        discount = bill_amount * 0.10
        print("Weekend bonus discount applied: 10%")
    else:
        discount = bill_amount * 0.05
        print("Weekday discount applied: 5%")

final_amount = bill_amount - discount
print(f"\nOriginal Bill : Rs. {bill_amount:.2f}")
print(f"Discount      : Rs. {discount:.2f}")
print(f"Final Amount  : Rs. {final_amount:.2f}")

# ============================================================
# END OF DAY 07
# ============================================================