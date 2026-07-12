"""
🐍 Day 30: Mini Project — Student Management System
Combines everything from Day 21-29:
Lists, Slicing, Nested Lists, List Comprehension,
Tuples, Sets, Dictionaries, Dict Comprehension
"""

# ----------------------------------------------------
# 1. Data Setup (list of dictionaries)
# ----------------------------------------------------

students = [
    {"name": "Rahul",  "scores": [90, 85, 88]},
    {"name": "Priya",  "scores": [45, 60, 55]},
    {"name": "Anjali", "scores": [88, 92, 95]},
    {"name": "Vikram", "scores": [30, 40, 35]},
    {"name": "Sneha",  "scores": [70, 75, 80]},
]


# ----------------------------------------------------
# 2. Calculate average score for each student
# ----------------------------------------------------

for student in students:
    student["average"] = sum(student["scores"]) / len(student["scores"])

print("--- All Students with Averages ---")
for s in students:
    print(f"{s['name']}: scores={s['scores']} avg={s['average']:.2f}")


# ----------------------------------------------------
# 3. List comprehension: names of students who passed (avg >= 50)
# ----------------------------------------------------

passed_names = [s["name"] for s in students if s["average"] >= 50]
failed_names = [s["name"] for s in students if s["average"] < 50]

print("\nPassed:", passed_names)
print("Failed:", failed_names)


# ----------------------------------------------------
# 4. Dict comprehension: name -> average lookup table
# ----------------------------------------------------

average_lookup = {s["name"]: round(s["average"], 2) for s in students}
print("\nName -> Average lookup:", average_lookup)


# ----------------------------------------------------
# 5. Find topper using max() with a key function
# ----------------------------------------------------

topper = max(students, key=lambda s: s["average"])
print(f"\nTopper: {topper['name']} with average {topper['average']:.2f}")


# ----------------------------------------------------
# 6. Tuple: store immutable top-3 ranking (name, average)
# ----------------------------------------------------

ranking = sorted(students, key=lambda s: s["average"], reverse=True)
top_3 = tuple((s["name"], round(s["average"], 2)) for s in ranking[:3])

print("\n--- Top 3 (as tuple) ---")
for rank, (name, avg) in enumerate(top_3, start=1):
    print(f"{rank}. {name} - {avg}")


# ----------------------------------------------------
# 7. Set: unique subjects across all students (bonus data)
# ----------------------------------------------------

subjects_taken = [
    ["Math", "Science"],
    ["Math", "English"],
    ["Science", "English", "Math"],
]

all_subjects = set()
for subj_list in subjects_taken:
    all_subjects.update(subj_list)

print("\nUnique subjects offered:", all_subjects)


# ----------------------------------------------------
# 8. Nested list: class-wise seating chart (rows of names)
# ----------------------------------------------------

seating_chart = [
    passed_names[0:2] if len(passed_names) >= 2 else passed_names,
    failed_names
]
print("\nSeating chart (row by row):")
for row_num, row in enumerate(seating_chart, start=1):
    print(f"Row {row_num}: {row}")


# ----------------------------------------------------
# 9. Final Summary Report
# ----------------------------------------------------

print("\n========== SUMMARY REPORT ==========")
print(f"Total students : {len(students)}")
print(f"Passed         : {len(passed_names)}")
print(f"Failed         : {len(failed_names)}")
print(f"Class average  : {sum(s['average'] for s in students) / len(students):.2f}")
print(f"Topper         : {topper['name']}")
print("======================================")


"""
📝 Quick Recap — Skills used in this project:
- List of dicts to model real-world records
- List comprehension to filter pass/fail
- Dict comprehension to build lookup tables
- max() + lambda to find the topper
- sorted() + slicing to get top-3 ranking
- Tuple to store immutable ranking data
- Set to collect unique values
- Nested lists to represent grouped/tabular data
"""