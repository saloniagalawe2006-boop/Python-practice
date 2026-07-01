"""
DAY 20: STUDENT GRADE MANAGER
Phase 1 Final Project

Combines: variables, data types, input/output, strings, operators,
conditions, loops, functions, scope, arguments, string formatting, slicing.
"""

# ---------------------------------------------------------
# GLOBAL DATA STORE
# ---------------------------------------------------------
# students = {
#     "Alice": {"Math": 90, "Science": 85, "English": 78},
#     "Bob":   {"Math": 60, "Science": 70, "English": 65},
# }
students = {}


# ---------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------

def add_student():
    """Ask the user for a student's name and marks in multiple subjects."""
    name = input("Enter student name: ").strip().title()

    if name in students:
        print(f"  '{name}' already exists. Their record will be overwritten.\n")

    subjects = input("Enter subjects separated by commas (e.g. Math,Science,English): ")
    subject_list = [s.strip().title() for s in subjects.split(",") if s.strip()]

    if not subject_list:
        print(" No subjects entered. Student not added.\n")
        return

    marks = {}
    for subject in subject_list:
        while True:
            try:
                score = float(input(f"  Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("   Marks must be between 0 and 100.")
            except ValueError:
                print("   Please enter a valid number.")

    students[name] = marks
    print(f" Student '{name}' added successfully!\n")


def calculate_average(marks_dict):
    """Return the average of a student's marks (dict of subject: score)."""
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def assign_grade(average):
    """Convert a numeric average into a letter grade."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def search_student():
    """Look up and display a single student's full record."""
    if not students:
        print("  No students in the system yet.\n")
        return

    name = input("Enter student name to search: ").strip().title()

    if name not in students:
        print(f" No student named '{name}' found.\n")
        return

    marks = students[name]
    avg = calculate_average(marks)
    grade = assign_grade(avg)

    print(f"\n--- {name}'s Record ---")
    for subject, score in marks.items():
        print(f"  {subject:<12}: {score:>6.2f}")
    print(f"  {'Average':<12}: {avg:>6.2f}")
    print(f"  {'Grade':<12}: {grade:>6}\n")


def get_rankings():
    """Return a list of (name, average, grade) sorted by average, highest first."""
    ranked = []
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = assign_grade(avg)
        ranked.append((name, avg, grade))

    # Sort by average descending using a lambda key
    ranked.sort(key=lambda item: item[1], reverse=True)
    return ranked


def display_table():
    """Print a neatly formatted table of every student, their average, grade, and rank."""
    if not students:
        print("  No students in the system yet.\n")
        return

    ranked = get_rankings()

    print("\n" + "=" * 55)
    print(f"{'Rank':<6}{'Name':<15}{'Average':<12}{'Grade':<8}")
    print("=" * 55)

    for rank, (name, avg, grade) in enumerate(ranked, start=1):
        print(f"{rank:<6}{name:<15}{avg:<12.2f}{grade:<8}")

    print("=" * 55 + "\n")


def class_statistics():
    """Show highest average, lowest average, and overall class average."""
    if not students:
        print("  No students in the system yet.\n")
        return

    ranked = get_rankings()
    averages = [avg for _, avg, _ in ranked]

    class_avg = sum(averages) / len(averages)
    top_student = ranked[0]
    bottom_student = ranked[-1]

    print("\n--- Class Statistics ---")
    print(f"  Total Students   : {len(students)}")
    print(f"  Class Average    : {class_avg:.2f}")
    print(f"  Highest Average  : {top_student[0]} ({top_student[1]:.2f}, Grade {top_student[2]})")
    print(f"  Lowest Average   : {bottom_student[0]} ({bottom_student[1]:.2f}, Grade {bottom_student[2]})\n")


def delete_student():
    """Remove a student from the system."""
    if not students:
        print(" No students in the system yet.\n")
        return

    name = input("Enter student name to delete: ").strip().title()
    if name in students:
        del students[name]
        print(f"  '{name}' has been removed.\n")
    else:
        print(f" No student named '{name}' found.\n")


# ---------------------------------------------------------
# MENU SYSTEM
# ---------------------------------------------------------

def show_menu():
    """Print the main menu options."""
    print("=" * 40)
    print("   STUDENT GRADE MANAGER")
    print("=" * 40)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display Result Table")
    print("4. Class Statistics")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 40)


def main():
    """Main program loop — keeps running until the user exits."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            display_table()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\n Thanks for using Student Grade Manager. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()