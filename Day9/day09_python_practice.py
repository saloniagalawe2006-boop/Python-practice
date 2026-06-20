# ============================================================
# Day 09 - for Loops & range()
# File: day09_for_loops.py
# ============================================================


# ── SECTION 1: Your First for Loop ───────────────────────────

for number in range(5):
    print(number)

print("Loop finished!")


# ── SECTION 2: range() with start and stop ───────────────────

print("\n--- range(1, 6) ---")
for number in range(1, 6):
    print(number)


# ── SECTION 3: range() with start, stop, and step ────────────

print("\n--- range(0, 20, 2) — even numbers ---")
for number in range(0, 20, 2):
    print(number)

print("\n--- range(10, 0, -1) — countdown ---")
for number in range(10, 0, -1):
    print(number)


# ── SECTION 4: Looping Through a String ──────────────────────

print("\n--- Looping through 'Python' ---")
for letter in "Python":
    print(letter)


# ── SECTION 5: Looping Through a List ────────────────────────

fruits = ["apple", "banana", "mango", "grapes"]

print("\n--- Looping through a list ---")
for fruit in fruits:
    print(fruit)


# ── SECTION 6: Using enumerate() — getting index AND value ───

print("\n--- enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\n--- enumerate() starting from 1 ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# ── SECTION 7: for with break and continue ───────────────────

print("\n--- break example: stop at 'mango' ---")
for fruit in fruits:
    if fruit == "mango":
        print("Found mango! Stopping search.")
        break
    print(f"Checking: {fruit}")

print("\n--- continue example: skip 'banana' ---")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)


# ── SECTION 8: Nested for Loops ───────────────────────────────

print("\n--- Nested for loop: multiplication grid ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="   ")
    print()    # new line after each row


# ── SECTION 9: for-else ───────────────────────────────────────

print("\n--- for-else: search for an item ---")
search_item = "kiwi"

for fruit in fruits:
    if fruit == search_item:
        print(f"{search_item} found!")
        break
else:
    print(f"{search_item} not found in the list.")


# ── SECTION 10: Practical — Sum and Average using for ─────────

print("\n--- Sum and Average of numbers ---")
numbers = [12, 45, 7, 23, 56, 89, 34]

total = 0
for num in numbers:
    total += num

average = total / len(numbers)
print(f"Numbers: {numbers}")
print(f"Total  : {total}")
print(f"Average: {average:.2f}")


# ── SECTION 11: Practical — Multiplication Table with for ─────

print("\n--- Multiplication Table (for loop version) ---")
table_of = int(input("Enter a number for its table: "))

for multiplier in range(1, 11):
    print(f"  {table_of} x {multiplier:2} = {table_of * multiplier}")


# ── SECTION 12: Practical — Star Pattern ──────────────────────

print("\n--- Star Pattern ---")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)


# ── SECTION 13: Practical — Counting Vowels ───────────────────

print("\n--- Vowel Counter ---")
text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels in '{text}': {vowel_count}")

# ============================================================
# END OF DAY 09
# ============================================================