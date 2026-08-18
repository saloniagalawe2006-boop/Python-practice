# Student Grade Management System
# Author: Saloni
# Description: Calculate total marks, percentage, grade and result.

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def check_result(marks):
    if all(mark >= 40 for mark in marks):
        return "PASS"
    return "FAIL"


def display_result(name, roll_no, subjects, marks):
    total, percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    result = check_result(marks)

    print("\n" + "=" * 50)
    print("           STUDENT RESULT")
    print("=" * 50)

    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_no}")

    print("\nSubject-wise Marks:")
    print("-" * 50)

    for subject, mark in zip(subjects, marks):
        print(f"{subject:<25} {mark:>10}")

    print("-" * 50)
    print(f"Total Marks  : {total}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")

    print("=" * 50)


def main():
    print("=" * 50)
    print("       STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    subjects = [
        "Python",
        "Java",
        "Database Management",
        "Computer Networks",
        "Operating System"
    ]

    marks = []

    print("\nEnter marks out of 100:")

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")

            except ValueError:
                print("❌ Please enter a valid number.")

    display_result(name, roll_no, subjects, marks)


if __name__ == "__main__":
    main()