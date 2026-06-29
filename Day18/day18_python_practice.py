# ============================================================
# Mini Project: Unit Converter
# File: unit_converter_project.py
# ============================================================

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462


def show_menu():
    print("\n" + "=" * 40)
    print("        UNIT CONVERTER")
    print("=" * 40)
    print("  1. Km to Miles")
    print("  2. Miles to Km")
    print("  3. Celsius to Fahrenheit")
    print("  4. Fahrenheit to Celsius")
    print("  5. Kg to Pounds")
    print("  6. Pounds to Kg")
    print("  7. Exit")
    print("=" * 40)


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("  Invalid number. Try again.")


def run_converter():
    while True:
        show_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "7":
            print("\nGoodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\nInvalid choice!")
            continue

        value = get_number("Enter value: ")

        if choice == "1":
            print(f"Result: {value} km = {km_to_miles(value):.2f} miles")
        elif choice == "2":
            print(f"Result: {value} miles = {miles_to_km(value):.2f} km")
        elif choice == "3":
            print(f"Result: {value}°C = {celsius_to_fahrenheit(value):.2f}°F")
        elif choice == "4":
            print(f"Result: {value}°F = {fahrenheit_to_celsius(value):.2f}°C")
        elif choice == "5":
            print(f"Result: {value} kg = {kg_to_pounds(value):.2f} lbs")
        elif choice == "6":
            print(f"Result: {value} lbs = {pounds_to_kg(value):.2f} kg")


if __name__ == "__main__":
    run_converter()