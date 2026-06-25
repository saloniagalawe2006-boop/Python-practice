# ============================================================
# Day 14 - Scope & the global Keyword
# File: day14_scope_and_global.py
# ============================================================


# ── SECTION 1: Local Scope — Variables Inside a Function ─────

def my_function():
    local_var = "I exist only inside this function"
    print(local_var)

my_function()

# Now try to use local_var OUTSIDE the function:
# print(local_var)   # ❌ This would CRASH with: NameError: name 'local_var' is not defined
# (commented out so the rest of the program can still run)

print("local_var cannot be accessed here - it no longer exists outside the function.")


# ── SECTION 2: Global Scope — Variables Outside Any Function ──

global_var = "I exist everywhere in this file"

def show_global():
    print(global_var)   # functions CAN READ global variables without any special keyword

show_global()
print(global_var)        # also accessible directly here, at the top level


# ── SECTION 3: The Trap — Creating a Local Variable with the SAME Name ─

counter = 100    # this is a GLOBAL variable

def try_to_change():
    counter = 5   # ⚠️ This does NOT change the global counter!
    # This line CREATES a brand new LOCAL variable also called 'counter'
    # It only exists inside this function, and disappears after the function ends.
    print(f"  Inside function, counter = {counter}")

try_to_change()
print(f"Outside function, counter is still = {counter}")
# Output proves: the global counter (100) was NEVER touched!


# ── SECTION 4: Using global to ACTUALLY Modify a Global Variable ─

score = 0    # global variable

def increase_score():
    global score    # this tells Python: "Don't create a new local variable.
                     #  Use the EXISTING global one called 'score'."
    score += 10

print(f"\nScore before: {score}")
increase_score()
print(f"Score after calling increase_score() once: {score}")
increase_score()
increase_score()
print(f"Score after calling increase_score() two more times: {score}")


# ── SECTION 5: Function Parameters Are ALWAYS Local ───────────

def greet(name):
    name = name.upper()    # this change ONLY affects the LOCAL copy of 'name'
    print(f"  Inside function: {name}")

user_name = "rahul"
greet(user_name)
print(f"Outside function, user_name is still: {user_name}")
# The original variable outside is completely unaffected by what happens inside


# ── SECTION 6: Why Excessive use of global is Considered Bad Practice ─

# BAD PRACTICE EXAMPLE (works, but hard to track/debug in larger programs):
total_bad = 0

def add_to_total_bad(amount):
    global total_bad
    total_bad += amount

add_to_total_bad(50)
add_to_total_bad(30)
print(f"\n[Bad Practice] total_bad = {total_bad}")
# Problem: as your program grows, ANY function anywhere could silently change
# total_bad, making bugs very hard to trace. You'd have to check EVERY function.


# GOOD PRACTICE — use return values instead of global:
def add_to_total_good(current_total, amount):
    return current_total + amount

total_good = 0
total_good = add_to_total_good(total_good, 50)
total_good = add_to_total_good(total_good, 30)
print(f"[Good Practice] total_good = {total_good}")
# This is BETTER: the function clearly shows what it needs (current_total, amount)
# and clearly shows what it gives back. No hidden side effects.


# ── SECTION 7: Nested Functions and Scope (a sneak peek) ──────

def outer_function():
    outer_var = "I am from outer_function"

    def inner_function():
        # inner_function CAN read outer_var, because it's "enclosed" within outer_function
        print(f"  Inner function sees: {outer_var}")

    inner_function()

print("\n--- Nested Function Scope ---")
outer_function()


# ── SECTION 8: Practical — Bank Account Simulation (without global) ─

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("  Insufficient funds!")
        return balance
    return balance - amount

print("\n--- Bank Simulation (clean, no global) ---")
account_balance = 1000
print(f"Starting balance: {account_balance}")

account_balance = deposit(account_balance, 500)
print(f"After deposit of 500: {account_balance}")

account_balance = withdraw(account_balance, 300)
print(f"After withdrawal of 300: {account_balance}")

account_balance = withdraw(account_balance, 5000)
print(f"After failed withdrawal attempt: {account_balance}")


# ── SECTION 9: Practical — Visitor Counter (legitimately using global) ─

visitor_count = 0    # Sometimes global IS the right tool - e.g. a simple running counter

def register_visitor(visitor_name):
    global visitor_count
    visitor_count += 1
    print(f"  Visitor #{visitor_count}: {visitor_name}")

print("\n--- Visitor Counter ---")
register_visitor("Rahul")
register_visitor("Priya")
register_visitor("Anjali")
print(f"Total visitors today: {visitor_count}")


# ── SECTION 10: Demonstrating Scope with a Quiz Score Tracker ─

quiz_score = 0

def answer_question(is_correct):
    global quiz_score
    if is_correct:
        quiz_score += 10
        print("  Correct! +10 points")
    else:
        quiz_score -= 5
        print("  Wrong! -5 points")
    print(f"  Current score: {quiz_score}")

print("\n--- Quiz Score Tracker ---")
answer_question(True)
answer_question(True)
answer_question(False)
answer_question(True)
print(f"\nFinal quiz score: {quiz_score}")

# ============================================================
# END OF DAY 14
# ============================================================