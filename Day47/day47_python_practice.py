"""
🐍 Day 47: Working with JSON
"""

import json

# ----------------------------------------------------
# 1. What is JSON?
# ----------------------------------------------------
# JSON (JavaScript Object Notation) is a lightweight format
# for storing and exchanging data — used everywhere in APIs,
# config files, and web apps. It looks a LOT like a Python dict.


# ----------------------------------------------------
# 2. Python dict -> JSON string (serialization)
# ----------------------------------------------------

student = {
    "name": "Rahul",
    "age": 22,
    "is_passed": True,
    "scores": [90, 85, 88],
    "address": {"city": "Pune", "pincode": "411001"}
}

json_string = json.dumps(student)
print("JSON string:\n", json_string)
print("Type:", type(json_string))


# ----------------------------------------------------
# 3. Pretty-printing JSON with indentation
# ----------------------------------------------------

pretty_json = json.dumps(student, indent=4)
print("\nPretty JSON:\n", pretty_json)


# ----------------------------------------------------
# 4. JSON string -> Python dict (deserialization)
# ----------------------------------------------------

raw_json = '{"name": "Priya", "age": 21, "city": "Mumbai"}'
parsed = json.loads(raw_json)

print("\nParsed dict:", parsed)
print("Type:", type(parsed))
print("Accessing a value:", parsed["name"])


# ----------------------------------------------------
# 5. Writing JSON data to a file
# ----------------------------------------------------

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nJSON data written to student.json")


# ----------------------------------------------------
# 6. Reading JSON data from a file
# ----------------------------------------------------

with open("student.json", "r") as file:
    loaded_data = json.load(file)

print("\nData loaded from file:", loaded_data)
print("Student name from file:", loaded_data["name"])


# ----------------------------------------------------
# 7. JSON with a list of records (common API response shape)
# ----------------------------------------------------

students_list = [
    {"name": "Rahul", "score": 90},
    {"name": "Priya", "score": 85},
    {"name": "Anjali", "score": 95}
]

json_list = json.dumps(students_list, indent=2)
print("\nList of records as JSON:\n", json_list)


# ----------------------------------------------------
# 8. Type mapping: Python <-> JSON
# ----------------------------------------------------
# Python              JSON
# dict          <->   object {}
# list/tuple    <->   array []
# str           <->   string
# int/float     <->   number
# True/False    <->   true/false
# None          <->   null

data_with_none = {"middle_name": None, "active": True}
print("\nNone/Boolean mapping:", json.dumps(data_with_none))


# ----------------------------------------------------
# 9. Handling invalid JSON safely
# ----------------------------------------------------

broken_json = '{"name": "Vikram", "age": }'   # missing value -> invalid

print("\n--- Handling invalid JSON ---")
try:
    json.loads(broken_json)
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)


# ----------------------------------------------------
# 10. Cleanup demo file
# ----------------------------------------------------

import os
os.remove("student.json")
print("\nDemo file cleaned up.")


"""
📝 Quick Recap:
- import json
- json.dumps(python_obj)     -> convert Python object TO JSON string
- json.loads(json_string)    -> convert JSON string TO Python object
- json.dump(obj, file)       -> write Python object AS JSON to a file
- json.load(file)            -> read JSON from a file INTO Python object
- indent=4                   -> pretty-print JSON output
- JSON maps closely to Python dicts/lists, but uses true/false/null
- Always wrap json.loads()/json.load() in try/except for
  json.JSONDecodeError when parsing untrusted data
"""