"""
🐍 Day 32: Variable Scope — Local vs Global
"""

# ----------------------------------------------------
# 1. Global variable
# ----------------------------------------------------
# A variable defined OUTSIDE any function -> accessible everywhere

message = "I am global"

def show_message():
    print("Inside function:", message)   # can READ global variable

show_message()
print("Outside function:", message)


# ----------------------------------------------------
# 2. Local variable
# ----------------------------------------------------
# A variable defined INSIDE a function -> only exists inside it

def greet():
    local_msg = "I am local to greet()"
    print(local_msg)

greet()

print("\n--- Trying to access local variable outside ---")
try:
    print(local_msg)
except NameError as e:
    print("Error:", e)


# ----------------------------------------------------
# 3. Local variable SHADOWS global variable with same name
# ----------------------------------------------------

count = 10   # global

def change_count():
    count = 5   # this creates a NEW local variable, doesn't touch global
    print("Inside function, count =", count)

change_count()
print("Outside function, count =", count)   # still 10!


# ----------------------------------------------------
# 4. Using the 'global' keyword to modify a global variable
# ----------------------------------------------------

score = 0

def add_point():
    global score       # tells Python: use the OUTER 'score', not a new local one
    score += 1

print("\nBefore:", score)
add_point()
add_point()
add_point()
print("After 3 calls to add_point():", score)


# ----------------------------------------------------
# 5. Function parameters are always local
# ----------------------------------------------------

def square(n):
    n = n * n     # only changes the LOCAL copy of n
    return n

x = 5
result = square(x)
print(f"\nOriginal x = {x}, square(x) = {result}")


# ----------------------------------------------------
# 6. Nested functions and enclosing scope
# ----------------------------------------------------

def outer():
    outer_var = "I'm from outer()"

    def inner():
        print("Inner function sees:", outer_var)

    inner()

outer()


# ----------------------------------------------------
# 7. Real-world example: bank balance tracker
# ----------------------------------------------------

balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. New balance: {balance}")
    else:
        print("Insufficient balance!")

print("\n--- Bank Demo ---")
deposit(500)
withdraw(200)
withdraw(5000)


"""
📝 Quick Recap:
- Global variable : defined outside functions, readable everywhere
- Local variable   : defined inside a function, only exists there
- Same name inside a function creates a NEW local variable (shadowing)
- Use 'global var_name' inside a function to MODIFY a global variable
- Function parameters and variables created inside a function are local
- Prefer passing values in/out over overusing 'global' in real projects
"""