"""
🐍 Day 21: Lists — Create & Access
------------------------------------
A list is a single variable that can hold MULTIPLE values, in order.
Think of it like a numbered train with compartments — each compartment
holds one value, and each compartment has a position number (index)
starting from 0.
"""

# ----------------------------------------------------
# 1. Creating a List
# ----------------------------------------------------

students = ["Rahul", "Priya", "Anjali", "Vikram", "Sneha"]
#             [0]      [1]      [2]       [3]       [4]

print("Full list of students:", students)
print("Type of 'students':", type(students))


# ----------------------------------------------------
# 2. Accessing Items by Index (starts at 0)
# ----------------------------------------------------

print("\n--- Accessing items ---")
print("First student  (index 0):", students[0])
print("Third student  (index 2):", students[2])
print("Last student   (index 4):", students[4])

# Negative indexing — count from the END of the list
print("Last student   (index -1):", students[-1])
print("Second-last    (index -2):", students[-2])


# ----------------------------------------------------
# 3. Slicing — grabbing a range of items
# ----------------------------------------------------
# syntax: list[start : stop]  -> stop index is NOT included

print("\n--- Slicing ---")
print("First three students [0:3]:", students[0:3])
print("From index 2 onward  [2:] :", students[2:])
print("All except last      [:-1]:", students[:-1])


# ----------------------------------------------------
# 4. Lists can hold duplicates
# ----------------------------------------------------

scores = [90, 85, 90, 70, 85]
print("\nScores list (duplicates allowed):", scores)


# ----------------------------------------------------
# 5. Lists can hold MIXED data types
# ----------------------------------------------------

mixed_list = ["Rahul", 22, True, 5.9]
print("\nMixed-type list:", mixed_list)
for item in mixed_list:
    print(f"  Value: {item!r}  ->  Type: {type(item).__name__}")


# ----------------------------------------------------
# 6. Finding the length of a list
# ----------------------------------------------------

print("\nNumber of students:", len(students))


# ----------------------------------------------------
# 7. Looping through a list
# ----------------------------------------------------

print("\n--- Looping through students ---")
for index, name in enumerate(students):
    print(f"Compartment [{index}] -> {name}")


# ----------------------------------------------------
# 8. Checking if a value exists in a list
# ----------------------------------------------------

print("\n--- Membership check ---")
name_to_check = "Anjali"
if name_to_check in students:
    print(f"{name_to_check} is in the list!")
else:
    print(f"{name_to_check} is NOT in the list.")


"""
📝 Quick Recap:
- List  = [item1, item2, item3, ...]
- Access by index: my_list[0], my_list[-1]
- Slice a range:   my_list[start:stop]
- len(my_list)     -> number of items
- Lists are ordered, mutable, indexed, allow duplicates,
  and can mix data types.
"""