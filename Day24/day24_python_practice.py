"""
🐍 Day 24: Nested Lists (Lists inside Lists / 2D Lists)
"""

# ----------------------------------------------------
# 1. Creating a Nested List
# ----------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Full matrix:", matrix)


# ----------------------------------------------------
# 2. Accessing elements in a nested list
# ----------------------------------------------------

print("\n--- Accessing elements ---")
print("Row 0:", matrix[0])
print("Row 1, Column 2:", matrix[1][2])   # 6
print("Row 2, Column 0:", matrix[2][0])   # 7


# ----------------------------------------------------
# 3. Modifying a nested list
# ----------------------------------------------------

matrix[0][1] = 99
print("\nAfter modifying matrix[0][1]:", matrix)


# ----------------------------------------------------
# 4. Looping through a nested list
# ----------------------------------------------------

print("\n--- Looping through matrix ---")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ----------------------------------------------------
# 5. Real-world example: Students with multiple scores
# ----------------------------------------------------

students = [
    ["Rahul", 90, 85],
    ["Priya", 70, 95],
    ["Anjali", 88, 92]
]

print("\n--- Student records ---")
for student in students:
    name = student[0]
    scores = student[1:]
    print(f"{name}: {scores} -> Average: {sum(scores)/len(scores):.2f}")


# ----------------------------------------------------
# 6. Nested list comprehension (bonus)
# ----------------------------------------------------

flat = [value for row in matrix for value in row]
print("\nFlattened matrix:", flat)


"""
📝 Quick Recap:
- Nested list = a list containing other lists
- Access:  matrix[row][col]
- Modify:  matrix[row][col] = new_value
- Loop with nested for-loops (outer = rows, inner = columns)
- Great for grids, tables, matrices, and grouped records
"""