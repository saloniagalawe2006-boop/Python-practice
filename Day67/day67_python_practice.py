expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def show_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n--- All Expenses ---")

    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total:.2f}\n")


def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    if not summary:
        print("No expenses found.\n")
        return

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

    print()


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()