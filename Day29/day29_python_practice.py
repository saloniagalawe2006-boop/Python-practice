"""
🐍 Day 29: Dictionary Comprehension
"""

# ----------------------------------------------------
# 1. The old way (using a loop)
# ----------------------------------------------------

squares = {}
for i in range(1, 6):
    squares[i] = i * i

print("Squares (loop way):", squares)


# ----------------------------------------------------
# 2. The dictionary comprehension way
# ----------------------------------------------------
# syntax: {key_expr: value_expr for item in iterable}

squares_comp = {i: i * i for i in range(1, 6)}
print("Squares (comprehension):", squares_comp)


# ----------------------------------------------------
# 3. Dict comprehension with a condition (filter)
# ----------------------------------------------------
# syntax: {key: value for item in iterable if condition}

numbers = range(1, 11)
even_squares = {n: n * n for n in numbers if n % 2 == 0}
print("\nEven squares:", even_squares)


# ----------------------------------------------------
# 4. Building a dict from two lists (zip)
# ----------------------------------------------------

names = ["Rahul", "Priya", "Anjali"]
scores = [90, 85, 88]

name_score_map = {name: score for name, score in zip(names, scores)}
print("\nName-Score map:", name_score_map)


# ----------------------------------------------------
# 5. Transforming an existing dictionary
# ----------------------------------------------------

prices = {"apple": 100, "banana": 40, "mango": 150}

# Apply 10% discount to every price
discounted = {item: price * 0.9 for item, price in prices.items()}
print("\nOriginal prices:", prices)
print("Discounted prices:", discounted)


# ----------------------------------------------------
# 6. Swapping keys and values
# ----------------------------------------------------

swapped = {value: key for key, value in prices.items()}
print("\nSwapped dict:", swapped)


# ----------------------------------------------------
# 7. Real-world example: filter passing students
# ----------------------------------------------------

student_scores = {"Rahul": 90, "Priya": 45, "Anjali": 88, "Vikram": 30}

passed = {name: score for name, score in student_scores.items() if score >= 50}
print("\nStudents who passed:", passed)


# ----------------------------------------------------
# 8. If-else inside dict comprehension
# ----------------------------------------------------

result = {name: ("Pass" if score >= 50 else "Fail") for name, score in student_scores.items()}
print("\nResult status:", result)


"""
📝 Quick Recap:
- Basic:   {key: value for item in iterable}
- Filter:  {key: value for item in iterable if condition}
- If-else: {key: (val_if_true if cond else val_if_false) for item in iterable}
- zip(list1, list2) pairs up two lists into (key, value) tuples
- Dict comprehensions are shorter and faster than manual loops
  for building new dictionaries.
"""