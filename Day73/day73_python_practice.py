"""
🐍 Day 70: Milestone Mini Project — Expense Tracker CLI
Combines everything from Day 61-69:
argparse, collections, string formatting, enums,
magic methods, pathlib, async basics, functools, config
"""

import argparse
import json
from pathlib import Path
from enum import Enum
from dataclasses import dataclass, asdict, field
from collections import Counter, defaultdict
from datetime import date
from functools import total_ordering


# ----------------------------------------------------
# 1. Category enum (Day 64)
# ----------------------------------------------------

class Category(Enum):
    FOOD = "Food"
    TRAVEL = "Travel"
    SHOPPING = "Shopping"
    BILLS = "Bills"
    OTHER = "Other"


# ----------------------------------------------------
# 2. Expense dataclass with magic methods (Day 58 + Day 65)
# ----------------------------------------------------

@total_ordering
@dataclass
class Expense:
    title: str
    amount: float
    category: Category
    expense_date: str = field(default_factory=lambda: date.today().isoformat())

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __str__(self):
        return f"{self.expense_date} | {self.title:<15} | {self.category.value:<10} | ${self.amount:>8.2f}"

    def to_dict(self):
        d = asdict(self)
        d["category"] = self.category.value
        return d


# ----------------------------------------------------
# 3. ExpenseTracker -> uses pathlib + JSON for storage (Day 66 + Day 47)
# ----------------------------------------------------

class ExpenseTracker:
    def __init__(self, filepath: str = "expenses.json"):
        self.filepath = Path(filepath)
        self.expenses: list[Expense] = []
        self._load()

    def _load(self):
        if self.filepath.exists():
            data = json.loads(self.filepath.read_text())
            self.expenses = [
                Expense(d["title"], d["amount"], Category(d["category"]), d["expense_date"])
                for d in data
            ]

    def _save(self):
        data = [e.to_dict() for e in self.expenses]
        self.filepath.write_text(json.dumps(data, indent=2))

    def add_expense(self, title, amount, category: Category):
        expense = Expense(title, amount, category)
        self.expenses.append(expense)
        self._save()
        print(f"Added: {expense}")

    def total_spent(self) -> float:
        return sum(e.amount for e in self.expenses)     # generator expr

    def by_category(self) -> dict:
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e.category.value] += e.amount
        return dict(totals)

    def most_common_category(self):
        counts = Counter(e.category.value for e in self.expenses)
        return counts.most_common(1)[0] if counts else None

    def top_expense(self) -> Expense:
        return max(self.expenses) if self.expenses else None     # uses __lt__

    def show_all(self):
        print("\n--- All Expenses ---")
        for e in sorted(self.expenses):        # uses total_ordering
            print(e)


# ----------------------------------------------------
# 4. CLI setup with argparse (Day 61)
# ----------------------------------------------------

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add a new expense")
add_parser.add_argument("title", type=str)
add_parser.add_argument("amount", type=float)
add_parser.add_argument("--category", type=str, default="Other",
                         choices=[c.value for c in Category])

subparsers.add_parser("summary", help="Show spending summary")
subparsers.add_parser("list", help="List all expenses")


# ----------------------------------------------------
# 5. Simulating CLI usage (no real terminal input needed for demo)
# ----------------------------------------------------

tracker = ExpenseTracker("demo_expenses.json")

simulated_commands = [
    ["add", "Groceries", "45.50", "--category", "Food"],
    ["add", "Uber ride", "12.00", "--category", "Travel"],
    ["add", "Netflix", "15.99", "--category", "Bills"],
    ["add", "New shoes", "60.00", "--category", "Shopping"],
    ["add", "Coffee", "5.25", "--category", "Food"],
]

print("--- Simulating CLI commands ---")
for cmd in simulated_commands:
    args = parser.parse_args(cmd)
    tracker.add_expense(args.title, args.amount, Category(args.category))


# ----------------------------------------------------
# 6. Displaying summary and listing (string formatting - Day 63)
# ----------------------------------------------------

tracker.show_all()

print(f"\n--- Summary ---")
print(f"Total spent: ${tracker.total_spent():.2f}")

print("\nSpending by category:")
for cat, amount in tracker.by_category().items():
    print(f"  {cat:<10}: ${amount:>8.2f}")

top_cat, top_count = tracker.most_common_category()
print(f"\nMost frequent category: {top_cat} ({top_count} expenses)")

print(f"Biggest single expense: {tracker.top_expense()}")


# ----------------------------------------------------
# 7. Cleanup
# ----------------------------------------------------

tracker.filepath.unlink()
print("\nDemo file cleaned up.")


"""
📝 Quick Recap — Skills used in this milestone project:
- argparse with subcommands for a real CLI structure
- Enum for expense categories (type-safe, self-documenting)
- Dataclass + total_ordering + custom __str__/__eq__/__lt__
- pathlib + JSON for simple persistent storage
- Counter/defaultdict for spending analysis
- f-string formatting for aligned, readable console output
- This mirrors a real personal-finance CLI tool!
"""