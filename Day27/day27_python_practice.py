"""
🐍 Day 27: Sets
"""

# ----------------------------------------------------
# 1. Creating a Set
# ----------------------------------------------------
# syntax: {item1, item2, item3, ...}
# A set stores UNIQUE items only, in NO fixed order

fruits = {"apple", "banana", "cherry", "apple"}   # duplicate "apple" auto-removed
print("Fruits set:", fruits)
print("Type:", type(fruits))

empty_set = set()   # NOT {} -> that creates an empty dict!
print("Empty set:", empty_set, type(empty_set))


# ----------------------------------------------------
# 2. Sets automatically remove duplicates
# ----------------------------------------------------

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print("\nOriginal list:", numbers)
print("Unique numbers (set):", unique_numbers)


# ----------------------------------------------------
# 3. Adding and removing items
# ----------------------------------------------------

colors = {"red", "green", "blue"}

colors.add("yellow")
print("\nAfter add('yellow'):", colors)

colors.remove("red")
print("After remove('red'):", colors)

colors.discard("purple")   # discard = no error even if item doesn't exist
print("After discard('purple') [no error]:", colors)


# ----------------------------------------------------
# 4. Sets are UNORDERED -> no indexing allowed
# ----------------------------------------------------

print("\n--- No indexing demo ---")
try:
    print(colors[0])
except TypeError as e:
    print("Error:", e)


# ----------------------------------------------------
# 5. Looping through a set
# ----------------------------------------------------

print("\n--- Looping ---")
for color in colors:
    print("Color:", color)


# ----------------------------------------------------
# 6. Set operations (math-style)
# ----------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\n--- Set operations ---")
print("Union        (a | b):", a | b)          # all items from both
print("Intersection (a & b):", a & b)          # common items
print("Difference   (a - b):", a - b)          # in a but not b
print("Symmetric diff (a ^ b):", a ^ b)        # in a or b, not both


# ----------------------------------------------------
# 7. Membership check (very fast in sets)
# ----------------------------------------------------

print("\n--- Membership check ---")
print("Is 3 in set a?", 3 in a)
print("Is 10 in set a?", 10 in a)


# ----------------------------------------------------
# 8. Real-world example: removing duplicate entries
# ----------------------------------------------------

emails = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com"]
unique_emails = list(set(emails))
print("\nOriginal emails:", emails)
print("Unique emails:", unique_emails)


"""
📝 Quick Recap:
- Set = {item1, item2, ...}  -> curly brackets, unique items only
- Unordered: no indexing or slicing
- add(), remove(), discard() to modify
- Union (|), Intersection (&), Difference (-), Symmetric Diff (^)
- Great for removing duplicates and fast membership checks
"""