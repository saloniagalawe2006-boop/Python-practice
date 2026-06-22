# ============================================================
# Day 10 - Loop Control: break, continue, pass
# File: day10_loop_control.py
# ============================================================


# ── SECTION 1: break Recap — Stops the Loop Completely ───────

print("--- break example ---")
for i in range(1, 11):
    if i == 6:
        print("Reached 6. Breaking out!")
        break
    print(i)

print("After the loop (break only skipped 6,7,8,9,10)")


# ── SECTION 2: continue Recap — Skips Current Round Only ─────

print("\n--- continue example ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("After the loop (all rounds ran, even numbers just skipped printing)")


# ── SECTION 3: break and continue only affect the NEAREST loop ─

print("\n--- break in a nested loop ---")
for i in range(1, 4):
    print(f"Outer loop: i = {i}")
    for j in range(1, 4):
        if j == 2:
            print("    Inner break triggered!")
            break          # only breaks the INNER loop
        print(f"  Inner loop: j = {j}")

print("Notice: outer loop (i) kept running all 3 times!")


print("\n--- continue in a nested loop ---")
for i in range(1, 4):
    print(f"Outer loop: i = {i}")
    for j in range(1, 4):
        if j == 2:
            continue       # only skips this ROUND of the inner loop
        print(f"  Inner loop: j = {j}")


# ── SECTION 4: Using a flag variable to break BOTH loops ──────

print("\n--- Breaking out of BOTH loops using a flag ---")
found = False
target = 6

for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"  Checking {i} x {j} = {product}")
        if product == target:
            print(f"  Found it! {i} x {j} = {target}")
            found = True
            break          # breaks inner loop
    if found:
        break              # breaks outer loop too, because found is True


# ── SECTION 5: pass — Doing Nothing (Placeholder) ────────────

print("\n--- pass example ---")
for i in range(1, 6):
    if i == 3:
        pass               # literally does nothing, just a placeholder
        print("(pass executed - did nothing special)")
    print(i)


# ── SECTION 6: break with while True — Controlled Infinite Loop ─

print("\n--- Menu system using while True + break ---")
while True:
    print("\n1. Say Hello")
    print("2. Show Date Info")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        print("Hello there!")
    elif choice == "2":
        print("Today is Day 10 of the Python challenge!")
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break              # the ONLY way out of this infinite loop
    else:
        print("Invalid choice, try again.")


# ── SECTION 7: continue to Skip Invalid Data in a List ────────

print("\n--- Processing a list, skipping invalid entries ---")
raw_scores = [85, -1, 92, 78, -5, 100, 45]

print("Processing scores (skipping negative/invalid ones):")
valid_total = 0
valid_count = 0

for score in raw_scores:
    if score < 0:
        print(f"  Skipping invalid score: {score}")
        continue
    print(f"  Processing valid score: {score}")
    valid_total += score
    valid_count += 1

print(f"\nValid scores processed: {valid_count}")
print(f"Average of valid scores: {valid_total / valid_count:.2f}")


# ── SECTION 8: Practical — Prime Number Finder Using break ────

print("\n--- Prime Number Checker ---")
num = int(input("Enter a number to check if it's prime: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    for divisor in range(2, num):
        if num % divisor == 0:
            print(f"  {num} is divisible by {divisor} - not prime")
            is_prime = False
            break          # no need to keep checking once we find ONE divisor

if is_prime:
    print(f"{num} is a PRIME number!")
else:
    print(f"{num} is NOT a prime number.")


# ── SECTION 9: Practical — Search with break + for-else ───────

print("\n--- Searching for a specific student ---")
students = ["Rahul", "Priya", "Anjali", "Vikram", "Sneha"]
search_name = input("Enter a name to search: ").strip().title()

for index, student in enumerate(students):
    if student == search_name:
        print(f"{search_name} found at position {index + 1}!")
        break
else:
    print(f"{search_name} is not in the student list.")

# ============================================================
# END OF DAY 10
# ============================================================