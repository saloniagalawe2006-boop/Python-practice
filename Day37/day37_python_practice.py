"""
🐍 Day 37: File Handling — Read & Write
"""

# ----------------------------------------------------
# 1. Writing to a file ('w' mode -> creates/overwrites)
# ----------------------------------------------------

with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 37!\n")
    file.write("Learning file handling in Python.\n")

print("File written successfully.")


# ----------------------------------------------------
# 2. Reading the ENTIRE file at once
# ----------------------------------------------------

with open("sample.txt", "r") as file:
    content = file.read()

print("\n--- Full file content ---")
print(content)


# ----------------------------------------------------
# 3. Reading line by line
# ----------------------------------------------------

print("--- Reading line by line ---")
with open("sample.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())   # strip() removes the trailing \n


# ----------------------------------------------------
# 4. Reading all lines into a list
# ----------------------------------------------------

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nAll lines as a list:", lines)


# ----------------------------------------------------
# 5. Appending to a file ('a' mode -> adds without erasing)
# ----------------------------------------------------

with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

with open("sample.txt", "r") as file:
    print("\n--- After appending ---")
    print(file.read())


# ----------------------------------------------------
# 6. Why use 'with open(...)'?
# ----------------------------------------------------
# 'with' automatically CLOSES the file when done,
# even if an error occurs inside the block.
# Without 'with', you'd need to manually call file.close()

# Manual way (not recommended, easy to forget close()):
file = open("sample.txt", "r")
data = file.read()
file.close()


# ----------------------------------------------------
# 7. Handling missing files safely
# ----------------------------------------------------

print("\n--- Handling missing file ---")
try:
    with open("does_not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found!")


# ----------------------------------------------------
# 8. Real-world example: saving student records to a file
# ----------------------------------------------------

students = ["Rahul,90", "Priya,85", "Anjali,95"]

with open("students.txt", "w") as file:
    for record in students:
        file.write(record + "\n")

print("\n--- Student records file ---")
with open("students.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(",")
        print(f"Name: {name}, Score: {score}")


# ----------------------------------------------------
# 9. Cleanup — remove the demo files
# ----------------------------------------------------

import os
os.remove("sample.txt")
os.remove("students.txt")
print("\nDemo files cleaned up.")


"""
📝 Quick Recap:
- 'w' mode -> write (overwrites existing content)
- 'a' mode -> append (adds to the end, keeps old content)
- 'r' mode -> read (default mode)
- with open(filename, mode) as file:  -> auto-closes the file safely
- file.read()       -> reads whole file as one string
- file.readlines()  -> reads all lines into a list
- for line in file: -> reads line by line (memory efficient)
- Always wrap file reads in try/except for FileNotFoundError
"""