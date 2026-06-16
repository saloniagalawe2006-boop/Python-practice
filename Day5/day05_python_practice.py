# ============================================================
# Day 05 - Operators
# File: day05_operators.py
# ============================================================


# ── SECTION 1: Arithmetic Operators ──────────────────────────

a = 20
b = 6

print(a + b)     # 26   → Addition
print(a - b)     # 14   → Subtraction
print(a * b)     # 120  → Multiplication
print(a / b)     # 3.3333... → Division (ALWAYS gives float)
print(a // b)    # 3    → Floor Division (drops decimal, no rounding)
print(a % b)     # 2    → Modulus (remainder after division)
print(a ** b)    # 64000000 → Exponent (20 to the power of 6)


# ── SECTION 2: Understanding // and % in depth ───────────────

print(20 // 6)   # 3    → 20 divided by 6 = 3 remainder 2 → floor is 3
print(20 % 6)    # 2    → the leftover remainder is 2

print(10 // 3)   # 3    → 10 divided by 3 = 3 remainder 1
print(10 % 3)    # 1    → remainder is 1

print(15 % 2)    # 1    → odd number  (remainder 1 when divided by 2)
print(16 % 2)    # 0    → even number (remainder 0 when divided by 2)


# ── SECTION 3: BODMAS — Order of Operations ──────────────────

print(2 + 3 * 4)        # 14 → NOT 20! Multiplication happens first
print((2 + 3) * 4)      # 20 → parentheses force addition first
print(10 - 2 + 3)       # 11 → left to right when same priority
print(2 ** 3 ** 2)      # 512 → exponent goes right to left: 3**2=9, then 2**9=512
print(10 / 2 * 5)       # 25.0 → left to right: 10/2=5.0, then 5.0*5=25.0


# ── SECTION 4: Comparison Operators ──────────────────────────

x = 10
y = 20

print(x == y)    # False → is x equal to y?
print(x != y)    # True  → is x NOT equal to y?
print(x > y)     # False → is x greater than y?
print(x < y)     # True  → is x less than y?
print(x >= 10)   # True  → is x greater than OR equal to 10?
print(x <= 9)    # False → is x less than OR equal to 9?

print(10 == 10.0)  # True  → int and float can be equal
print("a" == "A")  # False → comparison is case sensitive


# ── SECTION 5: Logical Operators ─────────────────────────────

age     = 20
has_id  = True

print(age >= 18 and has_id == True)   # True  → BOTH are true
print(age >= 18 and has_id == False)  # False → second part fails

print(age < 18 or has_id == True)     # True  → at least ONE is true
print(age < 18 or has_id == False)    # False → BOTH fail

print(not True)                        # False → flips True to False
print(not False)                       # True  → flips False to True
print(not (age < 18))                  # True  → age IS >= 18, so age<18 is False, not False = True


# ── SECTION 6: Assignment Operators ──────────────────────────

n = 10
print(n)        # 10

n += 5          # same as: n = n + 5
print(n)        # 15

n -= 3          # same as: n = n - 3
print(n)        # 12

n *= 2          # same as: n = n * 2
print(n)        # 24

n //= 5         # same as: n = n // 5
print(n)        # 4

n **= 3         # same as: n = n ** 3
print(n)        # 64

n %= 10         # same as: n = n % 10
print(n)        # 4


# ── SECTION 7: String Operators ──────────────────────────────

first  = "Hello"
second = "World"

print(first + " " + second)   # Hello World  → + joins strings
print(first * 3)              # HelloHelloHello → * repeats string
print("-" * 30)               # ------------------------------ → neat divider trick


# ── SECTION 8: Practical — Simple Calculator ─────────────────

print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

print()
print(f"  {num1} + {num2}  = {num1 + num2}")
print(f"  {num1} - {num2}  = {num1 - num2}")
print(f"  {num1} * {num2}  = {num1 * num2}")
print(f"  {num1} / {num2}  = {num1 / num2:.2f}")
print(f"  {num1} // {num2} = {num1 // num2}")
print(f"  {num1} % {num2}  = {num1 % num2}")
print(f"  {num1} ** {num2} = {num1 ** num2}")


# ── SECTION 9: Practical — Even or Odd Checker ───────────────

print("\n--- Even or Odd ---")
number = int(input("Enter any whole number: "))

remainder = number % 2
print(f"  {number} divided by 2 gives remainder: {remainder}")
print(f"  Is even: {remainder == 0}")
print(f"  Is odd : {remainder != 0}")


# ── SECTION 10: Practical — BMI Calculator ───────────────────

print("\n--- BMI Calculator ---")
weight = float(input("Your weight in kg : "))
height = float(input("Your height in m  : "))

bmi = weight / (height ** 2)

print(f"\n  Weight : {weight} kg")
print(f"  Height : {height} m")
print(f"  BMI    : {bmi:.2f}")
print()
print(f"  Underweight (BMI < 18.5)       : {bmi < 18.5}")
print(f"  Normal weight (18.5 to 24.9)   : {18.5 <= bmi <= 24.9}")
print(f"  Overweight  (BMI > 24.9)       : {bmi > 24.9}")


# ============================================================
# END OF DAY 05
# ============================================================