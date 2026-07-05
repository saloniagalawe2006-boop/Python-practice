# ============================================================
# Day 23 - List Slicing (Advanced)
# File: day23_list_slicing.py
# ============================================================


# ── SECTION 1: Basic List Slicing Recap ───────────────────────

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[0:5])      # [10, 20, 30, 40, 50]
print(numbers[3:7])      # [40, 50, 60, 70]
print(numbers[:4])       # [10, 20, 30, 40]
print(numbers[6:])       # [70, 80, 90, 100]
print(numbers[:])        # entire list (a full copy)


# ── SECTION 2: Step in List Slicing ───────────────────────────

print(numbers[::2])      # [10, 30, 50, 70, 90]   every 2nd item
print(numbers[1::2])     # [20, 40, 60, 80, 100]  every 2nd starting at index 1
print(numbers[::-1])     # reversed entire list
print(numbers[8:2:-1])   # [90, 80, 70, 60, 50, 40] backward from 8 to 3


# ── SECTION 3: Slicing Creates a NEW List (not a reference) ───

original = [1, 2, 3, 4, 5]
sliced   = original[1:4]    # creates a brand new list [2, 3, 4]

sliced[0] = 99
print(f"original: {original}")  # [1, 2, 3, 4, 5]  unchanged!
print(f"sliced  : {sliced}")    # [99, 3, 4]  only sliced changed


# ── SECTION 4: Using Slicing to REPLACE Part of a List ────────

items = [1, 2, 3, 4, 5, 6, 7]
items[2:5] = [30, 40, 50]
# replaces items at index 2,3,4 with the new values
print(items)
# [1, 2, 30, 40, 50, 6, 7]

items[1:3] = [200, 300, 400, 500]
# can replace with MORE items than you remove — list grows!
print(items)

items[1:5] = []
# replace with empty list = DELETE those items
print(items)


# ── SECTION 5: Slice Assignment with Different Sizes ──────────

letters = ["a", "b", "c", "d", "e"]
letters[1:3] = ["X", "Y", "Z"]
# replaced 2 items with 3 — list gets longer
print(letters)   # ['a', 'X', 'Y', 'Z', 'd', 'e']

letters[1:4] = []
# delete those 3 items
print(letters)   # ['a', 'd', 'e']


# ── SECTION 6: Unpacking a List ───────────────────────────────

point = [10, 20, 30]
x, y, z = point
# each variable gets one item from the list, left to right
print(f"x={x}, y={y}, z={z}")

first, *rest = [1, 2, 3, 4, 5]
# * collects everything that's left into a new list
print(f"first={first}, rest={rest}")

*beginning, last = [1, 2, 3, 4, 5]
print(f"beginning={beginning}, last={last}")

first2, *middle, last2 = [1, 2, 3, 4, 5]
print(f"first2={first2}, middle={middle}, last2={last2}")


# ── SECTION 7: Practical — Splitting a List into Halves ────────

data = [10, 20, 30, 40, 50, 60, 70, 80]
mid  = len(data) // 2

first_half  = data[:mid]
second_half = data[mid:]
print(f"Full      : {data}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")


# ── SECTION 8: Practical — Rotating a List ────────────────────

def rotate_left(lst, n):
    n = n % len(lst)    # handle n larger than list length
    return lst[n:] + lst[:n]

def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

items2 = [1, 2, 3, 4, 5]
print(f"\nOriginal       : {items2}")
print(f"Rotate left  2 : {rotate_left(items2, 2)}")
print(f"Rotate right 1 : {rotate_right(items2, 1)}")


# ── SECTION 9: Practical — Chunking a List ────────────────────

def chunk_list(lst, chunk_size):
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunks.append(lst[i:i + chunk_size])
    return chunks

data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nOriginal   : {data2}")
print(f"Chunks of 3: {chunk_list(data2, 3)}")
print(f"Chunks of 4: {chunk_list(data2, 4)}")


# ── SECTION 10: Practical — Removing Duplicates Using Slicing ──

def remove_duplicates(lst):
    seen    = []
    result  = []
    for item in lst:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

dupes = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print(f"\nWith duplicates   : {dupes}")
print(f"Without duplicates: {remove_duplicates(dupes)}")


# ── SECTION 11: Practical — Batch Student Processor ───────────

print("\n--- Batch Student Processor ---")
all_scores = [88, 45, 92, 67, 78, 55, 91, 34, 76, 83]

top_5      = sorted(all_scores, reverse=True)[:5]
bottom_5   = sorted(all_scores)[:5]
passed     = [s for s in all_scores if s >= 40]
failed     = [s for s in all_scores if s < 40]

print(f"All scores : {all_scores}")
print(f"Top 5      : {top_5}")
print(f"Bottom 5   : {bottom_5}")
print(f"Passed     : {passed}")
print(f"Failed     : {failed}")
print(f"Pass rate  : {len(passed)/len(all_scores)*100:.1f}%")


# ── SECTION 12: Practical — Interactive List Slicer ───────────

print("\n--- Interactive List Slicer ---")
user_list = []

print("Enter 8 numbers:")
for i in range(8):
    while True:
        try:
            num = int(input(f"  Number {i+1}: "))
            user_list.append(num)
            break
        except ValueError:
            print("  Enter a valid whole number!")

print(f"\nYour list     : {user_list}")
print(f"First 3       : {user_list[:3]}")
print(f"Last 3        : {user_list[-3:]}")
print(f"Middle        : {user_list[2:6]}")
print(f"Every 2nd     : {user_list[::2]}")
print(f"Reversed      : {user_list[::-1]}")
print(f"Sorted        : {sorted(user_list)}")
print(f"Max: {max(user_list)}, Min: {min(user_list)}, Sum: {sum(user_list)}")

# ============================================================
# END OF DAY 23
# ============================================================