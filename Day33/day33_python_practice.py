"""
🐍 Day 33: Lambda Functions (Anonymous Functions)
"""

# ----------------------------------------------------
# 1. Normal function vs Lambda function
# ----------------------------------------------------
# syntax: lambda arguments: expression

def square_normal(n):
    return n * n

square_lambda = lambda n: n * n

print("Normal function:", square_normal(5))
print("Lambda function:", square_lambda(5))


# ----------------------------------------------------
# 2. Lambda with multiple arguments
# ----------------------------------------------------

add = lambda a, b: a + b
print("\nAdd (lambda):", add(3, 7))

multiply = lambda a, b, c: a * b * c
print("Multiply (lambda):", multiply(2, 3, 4))


# ----------------------------------------------------
# 3. Lambda with no arguments
# ----------------------------------------------------

greet = lambda: "Hello from lambda!"
print("\n", greet())


# ----------------------------------------------------
# 4. Lambda with if-else (conditional expression)
# ----------------------------------------------------

check_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print("\n7 is:", check_even_odd(7))
print("10 is:", check_even_odd(10))


# ----------------------------------------------------
# 5. Lambda used with sorted() -> custom sort key
# ----------------------------------------------------

students = [("Rahul", 90), ("Priya", 85), ("Anjali", 95)]

# sort by score (2nd item in tuple)
sorted_by_score = sorted(students, key=lambda s: s[1], reverse=True)
print("\nSorted by score (high to low):", sorted_by_score)

# sort by name length
sorted_by_name_length = sorted(students, key=lambda s: len(s[0]))
print("Sorted by name length:", sorted_by_name_length)


# ----------------------------------------------------
# 6. Lambda used with map() -> transform every item
# ----------------------------------------------------

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n * n, numbers))
print("\nSquared numbers (map):", squared)


# ----------------------------------------------------
# 7. Lambda used with filter() -> keep items matching a condition
# ----------------------------------------------------

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers (filter):", evens)


# ----------------------------------------------------
# 8. Lambda used with max()/min() -> find the topper
# ----------------------------------------------------

topper = max(students, key=lambda s: s[1])
print("\nTopper:", topper)


# ----------------------------------------------------
# 9. When to use lambda vs a normal function
# ----------------------------------------------------
# - Lambda: short, throwaway, one-line logic (great inside sorted/map/filter)
# - Normal function: multi-line logic, needs a name, reused many times


"""
📝 Quick Recap:
- Syntax: lambda args: expression
- No 'def', no name required (anonymous), no explicit 'return'
- Best used for SHORT, one-time logic
- Common partners: sorted(key=...), map(), filter(), max()/min()
- For anything longer or reused often, use a normal 'def' function instead
"""