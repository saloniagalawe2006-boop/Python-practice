"""
=====================================================
DAY 21 - PYTHON JOURNEY
TOPIC: Lists — Create & Access
=====================================================

Today we learn about LISTS — the most used data
structure in Python.

A list lets us store MANY values in a single variable,
instead of creating student1, student2, student3...

Think of a list like a numbered train:
    - The train = the list (one variable)
    - Each compartment = one item
    - Each compartment has a number (INDEX) starting at 0
"""

print("="*55)
print("PART 1: THE PROBLEM LISTS SOLVE")
print("="*55)

# ---- The "bad" way (without lists) ----
student1 = "Rahul"
student2 = "Priya"
student3 = "Anjali"

print("Without lists:")
print(student1, student2, student3)
print("Imagine doing this for 500 students... impossible!\n")


print("="*55)
print("PART 2: CREATING A LIST")
print("="*55)

# A list is created using square brackets [ ]
# Items are separated by commas

students = ["Rahul", "Priya", "Anjali", "Vikram", "Sneha"]
#             [0]      [1]      [2]       [3]       [4]

print("List of students:", students)
print("Type of 'students':", type(students))

# Lists can hold different data types
numbers   = [10, 25, 30, 45, 50]
booleans  = [True, False, True]
mixed     = ["Rahul", 22, True, 5.9]   # mixed data types allowed
empty_list = []                        # an empty list

print("\nNumbers list :", numbers)
print("Booleans list:", booleans)
print("Mixed list   :", mixed)
print("Empty list   :", empty_list)


print("\n" + "="*55)
print("PART 3: ACCESSING LIST ITEMS (INDEXING)")
print("="*55)

# Indexing starts from 0, NOT 1
print("First student  (index 0):", students[0])
print("Second student (index 1):", students[1])
print("Third student  (index 2):", students[2])

# Negative indexing -> counts from the END
# -1 = last item, -2 = second last, etc.
print("\nLast student     (index -1):", students[-1])
print("Second-last (index -2):", students[-2])


print("\n" + "="*55)
print("PART 4: SLICING A LIST (accessing a range)")
print("="*55)

# Syntax: list[start : end]  -> 'end' index is NOT included
print("First three students  (0 to 2):", students[0:3])
print("Middle students       (1 to 3):", students[1:4])
print("From index 2 to end  :", students[2:])
print("From start to index 3:", students[:3])
print("Entire list (copy)   :", students[:])

# Negative slicing
print("Last two students    :", students[-2:])


print("\n" + "="*55)
print("PART 5: KEY PROPERTIES OF LISTS (with proof)")
print("="*55)

# 1. ORDERED - items keep the order you inserted them in
print("1. Ordered ->", students, "(order preserved)")

# 2. MUTABLE - we CAN change values after creation
students[0] = "Rohan"   # changing "Rahul" to "Rohan"
print("2. Mutable -> after changing index 0:", students)

# 3. INDEXED - every item has a position
for i in range(len(students)):
    print(f"   Index {i} -> {students[i]}")

# 4. ALLOWS DUPLICATES - same value can repeat
scores = [90, 85, 90, 70, 90]
print("4. Duplicates allowed ->", scores,
      "(90 appears", scores.count(90), "times)")

# 5. MIXED TYPES - one list, many data types
print("5. Mixed types ->", mixed)


print("\n" + "="*55)
print("PART 6: USEFUL BUILT-IN FUNCTIONS")
print("="*55)

print("Length of students list :", len(students))
print("Max of numbers list     :", max(numbers))
print("Min of numbers list     :", min(numbers))
print("Sum of numbers list     :", sum(numbers))
print("Is 'Priya' in students? :", "Priya" in students)
print("Is 'Rahul' in students? :", "Rahul" in students)  # False, renamed above


print("\n" + "="*55)
print("PART 7: LOOPING THROUGH A LIST")
print("="*55)

print("Using a simple for loop:")
for student in students:
    print("  -", student)

print("\nUsing index with enumerate():")
for index, student in enumerate(students):
    print(f"  {index}: {student}")


print("\n" + "="*55)
print("MINI CHALLENGE FOR YOU")
print("="*55)
print("""
1. Create a list called 'fruits' with 5 fruit names.
2. Print the first and last fruit using indexing.
3. Print fruits from index 1 to 3 using slicing.
4. Change the 2nd fruit to something else.
5. Check if "Mango" exists in your list using 'in'.
""")

# Try writing your solution below this line: