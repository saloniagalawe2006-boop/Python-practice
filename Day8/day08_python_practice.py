# ============================================================
# Day 08 - while Loops
# File: day08_while_loops.py
# ============================================================


# ── SECTION 1: Your First while Loop ─────────────────────────

count = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1

print("Loop finished!")


# ── SECTION 2: Countdown Timer ───────────────────────────────

print("\n--- Countdown ---")
number = 10

while number > 0:
    print(number)
    number -= 1

print("Blast off! 🚀")


# ── SECTION 3: Sum of Numbers ────────────────────────────────

print("\n--- Sum from 1 to 100 ---")
total = 0
n     = 1

while n <= 100:
    total = total + n
    n     = n + 1

print(f"Sum of 1 to 100 = {total}")


# ── SECTION 4: User Input Loop (repeat until valid) ──────────

print("\n--- Positive Number Validator ---")

number2 = int(input("Enter a positive number: "))

while number2 <= 0:
    print("That is not positive! Try again.")
    number2 = int(input("Enter a positive number: "))

print(f"Thank you! You entered: {number2}")


# ── SECTION 5: break — Exit a Loop Early ─────────────────────

print("\n--- Secret Word Game ---")
secret = "python"

while True:
    guess = input("Guess the secret word: ").strip().lower()
    if guess == secret:
        print("Correct! You found the secret word!")
        break
    else:
        print("Wrong guess. Try again.")


# ── SECTION 6: continue — Skip Current Iteration ─────────────

print("\n--- Print odd numbers from 1 to 10 ---")

i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# ── SECTION 7: while with else ───────────────────────────────

print("\n--- while with else ---")

attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
else:
    print("All 3 attempts used. while loop ended normally.")


# ── SECTION 8: Multiplication Table ──────────────────────────

print("\n--- Multiplication Table ---")
table_of = int(input("Enter a number for its table: "))

multiplier = 1

while multiplier <= 10:
    result = table_of * multiplier
    print(f"  {table_of} x {multiplier:2} = {result}")
    multiplier += 1


# ── SECTION 9: Digit Counter ──────────────────────────────────

print("\n--- Digit Counter ---")
num = int(input("Enter any integer: "))

if num < 0:
    num = -num

digit_count = 0

while num > 0:
    num         = num // 10
    digit_count = digit_count + 1

print(f"Number of digits: {digit_count}")


# ── SECTION 10: ATM Withdrawal Loop ──────────────────────────

print("\n--- ATM Simulation ---")
balance  = 10000
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"\nCurrent balance: Rs. {balance}")
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount. Must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance!")
    elif amount % 100 != 0:
        print("Amount must be in multiples of Rs. 100.")
    else:
        balance -= amount
        print(f"Rs. {amount} dispensed successfully.")
        print(f"Remaining balance: Rs. {balance}")
        break

    attempts += 1
    if attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempt(s) left.")

if attempts == max_attempts:
    print("\nToo many failed attempts. Card blocked.")

# ============================================================
# END OF DAY 08
# ============================================================