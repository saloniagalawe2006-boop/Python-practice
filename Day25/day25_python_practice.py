"""
🐍 Day 25: List Comprehension
"""

# ----------------------------------------------------
# 1. The old way (using a loop)
# ----------------------------------------------------

squares = []
for i in range(1, 6):
    squares.append(i * i)

print("Squares (loop way):", squares)


# ----------------------------------------------------
# 2. The list comprehension way
# ----------------------------------------------------
# syntax: [expression for item in iterable]

squares_comp = [i * i for i in range(1, 6)]
print("Squares (comprehension):", squares_comp)


# ----------------------------------------------------
# 3. List comprehension with a condition (filter)
# ----------------------------------------------------
# syntax: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if n % 2 == 0]
print("\nEven numbers:", evens)

odds = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odds)


# ----------------------------------------------------
# 4. List comprehension with if-else (transform)
# ----------------------------------------------------
# syntax: [value_if_true if condition else value_if_false for item in iterable]

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("\nLabels:", labels)


# ----------------------------------------------------
# 5. Working with strings
# ----------------------------------------------------

names = ["rahul", "priya", "anjali", "vikram"]

capitalized = [name.capitalize() for name in names]
print("\nCapitalized names:", capitalized)

long_names = [name for name in names if len(name) > 5]
print("Names longer than 5 letters:", long_names)


# ----------------------------------------------------
# 6. Nested list comprehension (flatten a 2D list)
# ----------------------------------------------------

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print("\nFlattened matrix:", flat)


# ----------------------------------------------------
# 7. Real-world example: filter student scores
# ----------------------------------------------------

students = [
    ("Rahul", 90),
    ("Priya", 45),
    ("Anjali", 88),
    ("Vikram", 30)
]

passed = [name for name, score in students if score >= 50]
print("\nStudents who passed:", passed)


"""
📝 Quick Recap:
- Basic:     [expr for item in iterable]
- Filter:    [expr for item in iterable if condition]
- If-else:   [true_val if cond else false_val for item in iterable]
- Nested:    [val for row in matrix for val in row]
- List comprehensions are shorter and faster than manual loops
  for building new lists.
"""