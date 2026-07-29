"""
🐍 Day 48: Working with CSV Files
"""

import csv

# ----------------------------------------------------
# 1. What is a CSV file?
# ----------------------------------------------------
# CSV = Comma-Separated Values. A simple text format for
# storing tabular data (like a spreadsheet), where each
# row is a line and each column is separated by a comma.


# ----------------------------------------------------
# 2. Writing data to a CSV file
# ----------------------------------------------------

students = [
    ["Name", "Age", "Score"],     # header row
    ["Rahul", 22, 90],
    ["Priya", 21, 85],
    ["Anjali", 23, 95]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file written successfully.")


# ----------------------------------------------------
# 3. Reading a CSV file (basic way)
# ----------------------------------------------------

print("\n--- Reading CSV (basic) ---")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# ----------------------------------------------------
# 4. Reading a CSV file as dictionaries (DictReader)
# ----------------------------------------------------
# Each row becomes a dict using the header as keys — much
# easier to work with than plain lists.

print("\n--- Reading CSV as dictionaries ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(f"  Name: {row['Name']}, Score: {row['Score']}")


# ----------------------------------------------------
# 5. Writing dictionaries to a CSV file (DictWriter)
# ----------------------------------------------------

employee_data = [
    {"Name": "Vikram", "Department": "IT", "Salary": 55000},
    {"Name": "Sneha", "Department": "HR", "Salary": 48000}
]

with open("employees.csv", "w", newline="") as file:
    fieldnames = ["Name", "Department", "Salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()          # writes the header row
    writer.writerows(employee_data)

print("\nemployees.csv written using DictWriter.")

with open("employees.csv", "r") as file:
    print(file.read())


# ----------------------------------------------------
# 6. Appending a new row to an existing CSV
# ----------------------------------------------------

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Vikram", 24, 78])

print("--- After appending a new student ---")
with open("students.csv", "r") as file:
    print(file.read())


# ----------------------------------------------------
# 7. Real-world example: calculating average score from CSV
# ----------------------------------------------------

total_score = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_score += int(row["Score"])
        count += 1

print(f"Average score across {count} students: {total_score / count:.2f}")


# ----------------------------------------------------
# 8. Handling different delimiters (e.g., tab or semicolon)
# ----------------------------------------------------

with open("data_semicolon.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Item", "Price"])
    writer.writerow(["Book", 250])

print("\n--- Reading semicolon-delimited file ---")
with open("data_semicolon.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)


# ----------------------------------------------------
# 9. Cleanup demo files
# ----------------------------------------------------

import os
os.remove("students.csv")
os.remove("employees.csv")
os.remove("data_semicolon.csv")
print("\nDemo files cleaned up.")


"""
📝 Quick Recap:
- import csv
- csv.writer(file).writerow(row) / writerows(list_of_rows)
- csv.reader(file) -> reads rows as plain lists
- csv.DictReader(file) -> reads rows as dictionaries (uses header)
- csv.DictWriter(file, fieldnames=...) -> writes dicts as CSV rows
- Always open CSV files with newline="" to avoid extra blank lines
- delimiter=";" -> customize the separator character if needed
- CSV is the go-to format for spreadsheets, data exports, and
  simple data storage without needing a database
"""