"""
🐍 Day 26: Tuples
"""

# ----------------------------------------------------
# 1. Creating a Tuple
# ----------------------------------------------------
# syntax: (item1, item2, item3, ...)

coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = ("apple",)   # comma is required for a single-item tuple!
empty_tuple = ()

print("Coordinates:", coordinates)
print("Colors:", colors)
print("Single item tuple:", single_item)
print("Type:", type(coordinates))


# ----------------------------------------------------
# 2. Accessing items (same as lists)
# ----------------------------------------------------

print("\n--- Accessing items ---")
print("First color:", colors[0])
print("Last color (negative index):", colors[-1])
print("Slice [0:2]:", colors[0:2])


# ----------------------------------------------------
# 3. Tuples are IMMUTABLE (cannot be changed)
# ----------------------------------------------------

print("\n--- Immutability demo ---")
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)


# ----------------------------------------------------
# 4. Looping through a tuple
# ----------------------------------------------------

print("\n--- Looping ---")
for color in colors:
    print("Color:", color)


# ----------------------------------------------------
# 5. Tuple unpacking
# ----------------------------------------------------

point = (5, 15)
x, y = point
print(f"\nUnpacked point -> x={x}, y={y}")

name, age, city = ("Rahul", 22, "Pune")
print(f"Unpacked person -> name={name}, age={age}, city={city}")


# ----------------------------------------------------
# 6. Tuple vs List — key differences
# ----------------------------------------------------

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list.append(4)          # works, lists are mutable
print("\nList after append:", my_list)

# my_tuple.append(4)       # would raise AttributeError, tuples have no append


# ----------------------------------------------------
# 7. Why use tuples?
# ----------------------------------------------------
# - Faster than lists
# - Protects data from accidental changes
# - Used for fixed data: coordinates, RGB colors, database records

rgb = (255, 0, 0)
print("\nFixed RGB value (should never change):", rgb)


# ----------------------------------------------------
# 8. Useful tuple methods
# ----------------------------------------------------

numbers = (1, 2, 2, 3, 4, 2)
print("\nCount of 2:", numbers.count(2))
print("Index of first 3:", numbers.index(3))
print("Length:", len(numbers))


"""
📝 Quick Recap:
- Tuple = (item1, item2, ...)  -> uses ROUND brackets
- Immutable: cannot add, remove, or change items after creation
- Supports indexing, slicing, looping — just like lists
- Unpacking: x, y = (10, 20)
- Use tuples for fixed/constant data; use lists for changeable data
"""