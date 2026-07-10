"""
🐍 Day 28: Dictionaries
"""

# ----------------------------------------------------
# 1. Creating a Dictionary
# ----------------------------------------------------
# syntax: {key1: value1, key2: value2, ...}
# Stores data as KEY -> VALUE pairs

student = {
    "name": "Rahul",
    "age": 22,
    "city": "Pune"
}

print("Student dict:", student)
print("Type:", type(student))


# ----------------------------------------------------
# 2. Accessing values by key
# ----------------------------------------------------

print("\n--- Accessing values ---")
print("Name:", student["name"])
print("Age:", student["age"])

# .get() is safer -> won't crash if key doesn't exist
print("Phone (using get):", student.get("phone"))
print("Phone (with default):", student.get("phone", "Not Available"))


# ----------------------------------------------------
# 3. Adding and updating values
# ----------------------------------------------------

student["phone"] = "9876543210"   # add new key
student["age"] = 23               # update existing key

print("\nAfter add/update:", student)


# ----------------------------------------------------
# 4. Removing items
# ----------------------------------------------------

removed_value = student.pop("phone")
print("\nRemoved phone:", removed_value)
print("After pop:", student)

del student["city"]
print("After del city:", student)


# ----------------------------------------------------
# 5. Looping through a dictionary
# ----------------------------------------------------

print("\n--- Looping through keys ---")
for key in student:
    print(key)

print("\n--- Looping through keys and values ---")
for key, value in student.items():
    print(f"{key} -> {value}")


# ----------------------------------------------------
# 6. Checking if a key exists
# ----------------------------------------------------

print("\n--- Membership check ---")
print("Is 'name' a key?", "name" in student)
print("Is 'city' a key?", "city" in student)


# ----------------------------------------------------
# 7. Useful dictionary methods
# ----------------------------------------------------

print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))


# ----------------------------------------------------
# 8. Nested dictionary (real-world example)
# ----------------------------------------------------

students = {
    "s1": {"name": "Rahul", "score": 90},
    "s2": {"name": "Priya", "score": 85}
}

print("\n--- Nested dictionary ---")
for student_id, info in students.items():
    print(f"{student_id}: {info['name']} scored {info['score']}")


"""
📝 Quick Recap:
- Dict = {key: value, ...}  -> curly brackets with key:value pairs
- Access: dict[key] or dict.get(key, default)
- Add/Update: dict[key] = value
- Remove: dict.pop(key) or del dict[key]
- Loop: for key in dict / for key, value in dict.items()
- Keys must be unique; values can be anything (even other dicts/lists)
"""