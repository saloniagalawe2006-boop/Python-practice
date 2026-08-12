"""
🐍 Day 61: Command-Line Arguments — argparse
"""

import argparse

# ----------------------------------------------------
# 1. Why command-line arguments?
# ----------------------------------------------------
# Instead of hardcoding values or asking for input() every time,
# CLI tools accept arguments directly when you run the script:
#
#   python script.py --name Rahul --age 22
#
# This is how real command-line tools (git, pip, ffmpeg) work.


# ----------------------------------------------------
# 2. Creating a basic parser
# ----------------------------------------------------

parser = argparse.ArgumentParser(description="Day 61 Demo: A simple greeting CLI tool")

# Positional argument -> REQUIRED, no dashes needed
parser.add_argument("name", type=str, help="The name to greet")

# Optional argument -> uses -- prefix, has a default
parser.add_argument("--greeting", type=str, default="Hello", help="Custom greeting word")

# Optional flag -> True/False switch, no value needed
parser.add_argument("--shout", action="store_true", help="Print the greeting in UPPERCASE")

# Optional argument with a type conversion
parser.add_argument("--times", type=int, default=1, help="How many times to repeat the greeting")


# ----------------------------------------------------
# 3. Parsing arguments
# ----------------------------------------------------
# In a real script this reads from sys.argv (the actual command line).
# Here, we simulate it manually so this demo runs without real CLI input.

simulated_args = ["Rahul", "--greeting", "Hey", "--times", "3", "--shout"]
args = parser.parse_args(simulated_args)

print("--- Parsed arguments ---")
print("name:", args.name)
print("greeting:", args.greeting)
print("shout:", args.shout)
print("times:", args.times)


# ----------------------------------------------------
# 4. Using the parsed arguments
# ----------------------------------------------------

message = f"{args.greeting}, {args.name}!"
if args.shout:
    message = message.upper()

print("\n--- Output ---")
for _ in range(args.times):
    print(message)


# ----------------------------------------------------
# 5. A more realistic example: a simple calculator CLI
# ----------------------------------------------------

calc_parser = argparse.ArgumentParser(description="Simple calculator CLI")
calc_parser.add_argument("a", type=float, help="First number")
calc_parser.add_argument("b", type=float, help="Second number")
calc_parser.add_argument("--op", choices=["add", "sub", "mul", "div"], default="add",
                          help="Operation to perform")

def calculate(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

print("\n--- Calculator CLI demo ---")
calc_args = calc_parser.parse_args(["10", "5", "--op", "mul"])
result = calculate(calc_args.a, calc_args.b, calc_args.op)
print(f"{calc_args.a} {calc_args.op} {calc_args.b} = {result}")


# ----------------------------------------------------
# 6. What --help automatically generates
# ----------------------------------------------------
# Running: python script.py --help
# automatically prints a nicely formatted usage guide
# built from your add_argument() calls -> no extra work needed!

print("\n--- Auto-generated help text ---")
parser.print_help()


# ----------------------------------------------------
# 7. Real-world pattern: how you'd write this for an ACTUAL script
# ----------------------------------------------------
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("--shout", action="store_true")
    args = parser.parse_args()          # reads real command-line input

    message = f"Hello, {args.name}!"
    if args.shout:
        message = message.upper()
    print(message)

# Then run from terminal like:
#   python script.py Rahul --shout
"""


"""
📝 Quick Recap:
- import argparse
- parser = argparse.ArgumentParser(description=...)
- parser.add_argument("name")        -> required positional argument
- parser.add_argument("--flag", ...) -> optional named argument
- action="store_true"                -> boolean flag (no value needed)
- type=int/float/str                 -> auto-converts the input
- default=...                        -> value used if not provided
- choices=[...]                      -> restrict to specific valid values
- args = parser.parse_args()         -> reads real sys.argv in a script
- --help is generated automatically from your argument definitions
"""