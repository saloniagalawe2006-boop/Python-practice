"""
🐍 Day 49: Useful Built-in Functions
map, filter, reduce, zip, enumerate, sorted, any, all
"""

from functools import reduce

# ----------------------------------------------------
# 1. map() -> apply a function to every item in an iterable
# ----------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda n: n ** 2, numbers))
print("Squared:", squared)

names = ["rahul", "priya", "anjali"]
capitalized = list(map(str.capitalize, names))
print("Capitalized:", capitalized)


# ----------------------------------------------------
# 2. filter() -> keep only items that match a condition
# ----------------------------------------------------

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("\nEven numbers:", evens)

long_names = list(filter(lambda n: len(n) > 5, names))
print("Names longer than 5 letters:", long_names)


# ----------------------------------------------------
# 3. reduce() -> combine ALL items into a single value
# ----------------------------------------------------
# Not built-in by default -> comes from functools

total = reduce(lambda a, b: a + b, numbers)
print("\nSum using reduce:", total)

product = reduce(lambda a, b: a * b, numbers)
print("Product using reduce:", product)

biggest = reduce(lambda a, b: a if a > b else b, numbers)
print("Max using reduce:", biggest)


# ----------------------------------------------------
# 4. zip() -> combine multiple iterables pair by pair
# ----------------------------------------------------

student_names = ["Rahul", "Priya", "Anjali"]
scores = [90, 85, 95]

zipped = list(zip(student_names, scores))
print("\nZipped pairs:", zipped)

for name, score in zip(student_names, scores):
    print(f"{name} scored {score}")

# zip() with 3 iterables
subjects = ["Math", "Science", "English"]
for name, score, subject in zip(student_names, scores, subjects):
    print(f"{name} scored {score} in {subject}")


# ----------------------------------------------------
# 5. enumerate() -> get index + value together while looping
# ----------------------------------------------------

print("\n--- enumerate() ---")
for index, name in enumerate(student_names):
    print(f"{index}: {name}")

print("\n--- enumerate() with custom start ---")
for index, name in enumerate(student_names, start=1):
    print(f"Rank {index}: {name}")


# ----------------------------------------------------
# 6. sorted() -> sort any iterable (returns a NEW list)
# ----------------------------------------------------

unsorted_scores = [90, 45, 88, 30, 75]
print("\nSorted (ascending):", sorted(unsorted_scores))
print("Sorted (descending):", sorted(unsorted_scores, reverse=True))

# sorting complex data with a key
students_scores = [("Rahul", 90), ("Priya", 45), ("Anjali", 88)]
sorted_by_score = sorted(students_scores, key=lambda s: s[1], reverse=True)
print("Sorted by score:", sorted_by_score)


# ----------------------------------------------------
# 7. any() and all() -> check conditions across a collection
# ----------------------------------------------------

scores_list = [90, 45, 88, 30, 75]

print("\nAny score >= 90?", any(score >= 90 for score in scores_list))
print("All scores >= 50?", all(score >= 50 for score in scores_list))
print("All scores >= 0?", all(score >= 0 for score in scores_list))


# ----------------------------------------------------
# 8. Real-world example: combining several of these together
# ----------------------------------------------------

records = [("Rahul", 90), ("Priya", 45), ("Anjali", 88), ("Vikram", 30)]

# Step 1: filter passing students
passing = list(filter(lambda r: r[1] >= 50, records))

# Step 2: map to just names
passing_names = list(map(lambda r: r[0], passing))

# Step 3: sort alphabetically
sorted_names = sorted(passing_names)

print("\n--- Combined pipeline ---")
print("Passing students (sorted):", sorted_names)


"""
📝 Quick Recap:
- map(func, iterable)     -> transforms every item
- filter(func, iterable)  -> keeps items matching a condition
- reduce(func, iterable)  -> combines all items into ONE value (functools)
- zip(iter1, iter2, ...)  -> pairs up multiple iterables together
- enumerate(iterable)     -> gives (index, value) pairs while looping
- sorted(iterable, key=...) -> returns a sorted NEW list
- any(iterable)  -> True if AT LEAST ONE item is truthy
- all(iterable)  -> True if ALL items are truthy
- These functions are the backbone of clean, functional-style Python
"""