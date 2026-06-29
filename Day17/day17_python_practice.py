# ============================================================
# Day 18 - Mini Project: Calculator
# File: day18_calculator_project.py
# Combines: functions, loops, conditions, input, formatting
# ============================================================


# ── SECTION 1: Calculation Functions (Day 11-13) ─────────────

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Error: Cannot divide by zero!"
    return a / b, "Success"

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return None, "Error: Cannot divide by zero!"
    return a % b, "Success"


# ── SECTION 2: Input Validation Function (Day 3, Day 12) ─────

def get_number(prompt):
    """Keeps asking until the user enters a valid number."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("  Invalid input! Please enter a valid number.")
            # try/except is a sneak peek of Day 44 - for now, just know it
            # safely catches the crash that int()/float() would normally cause
            # on invalid text, letting the loop ask again instead of crashing.


# ── SECTION 3: Menu Display Function (Day 15 formatting) ─────

def show_menu():
    print("\n" + "=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Power           (**)")
    print("  6. Modulus         (%)")
    print("  7. View History")
    print("  8. Exit")
    print("=" * 40)


# ── SECTION 4: History Tracking (list preview - Day 21) ───────

calculation_history = []     # an empty list to store past calculations

def add_to_history(operation, num1, num2, result):
    entry = f"{num1} {operation} {num2} = {result}"
    calculation_history.append(entry)
    # .append() adds a new item to the END of a list - full detail Day 21-22

def show_history():
    print("\n" + "-" * 40)
    print("       CALCULATION HISTORY")
    print("-" * 40)
    if not calculation_history:
        print("  No calculations yet.")
    else:
        for index, entry in enumerate(calculation_history, start=1):
            print(f"  {index}. {entry}")
    print("-" * 40)


# ── SECTION 5: Main Program Loop (Day 8/10 - while True + break) ─

def run_calculator():
    print("Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice == "7":
            show_history()
            continue   # skip the rest of the loop, go straight back to the menu

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\nInvalid choice! Please select a number from 1 to 8.")
            continue

        # Get the two numbers needed for the calculation
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        # Perform the calculation based on the menu choice
        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
            print(f"\nResult: {num1} + {num2} = {result}")
            add_to_history(symbol, num1, num2, result)

        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
            print(f"\nResult: {num1} - {num2} = {result}")
            add_to_history(symbol, num1, num2, result)

        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
            print(f"\nResult: {num1} * {num2} = {result}")
            add_to_history(symbol, num1, num2, result)

        elif choice == "4":
            result, status = divide(num1, num2)
            symbol = "/"
            if result is None:
                print(f"\n{status}")
            else:
                print(f"\nResult: {num1} / {num2} = {result:.4f}")
                add_to_history(symbol, num1, num2, round(result, 4))

        elif choice == "5":
            result = power(num1, num2)
            symbol = "**"
            print(f"\nResult: {num1} ** {num2} = {result}")
            add_to_history(symbol, num1, num2, result)

        elif choice == "6":
            result, status = modulus(num1, num2)
            symbol = "%"
            if result is None:
                print(f"\n{status}")
            else:
                print(f"\nResult: {num1} % {num2} = {result}")
                add_to_history(symbol, num1, num2, result)

        # Ask if the user wants to continue
        again = input("\nPerform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for using the calculator. Goodbye!")
            break


# ── SECTION 6: Program Entry Point ─────────────────────────────

if __name__ == "__main__":
    run_calculator()
    print("\n--- Final Calculation History ---")
    show_history()

# ============================================================
# END OF DAY 18
# ============================================================