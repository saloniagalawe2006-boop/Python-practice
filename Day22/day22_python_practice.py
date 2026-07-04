# ============================================================
# Day 22 - List Methods
# File: day22_list_methods.py
# ============================================================


# ── SECTION 1: append() — Add ONE item to the END ────────────

fruits = ["apple", "banana", "mango"]
fruits.append("grapes")
fruits.append("orange")
print(fruits)
# ['apple', 'banana', 'mango', 'grapes', 'orange']


# ── SECTION 2: insert() — Add item at a SPECIFIC position ────

fruits.insert(1, "blueberry")
# insert(index, value) → pushes everything else to the right
print(fruits)
# ['apple', 'blueberry', 'banana', 'mango', 'grapes', 'orange']

fruits.insert(0, "cherry")
# insert at index 0 = add to the very beginning
print(fruits)


# ── SECTION 3: extend() — Add MULTIPLE items at once ─────────

fruits.extend(["kiwi", "pineapple", "watermelon"])
# extend() joins another list into the current one
print(fruits)

# Difference: append() vs extend()
a = [1, 2, 3]
b = [1, 2, 3]
a.append([4, 5])    # adds the LIST ITSELF as one item → [1, 2, 3, [4, 5]]
b.extend([4, 5])    # adds each item individually   → [1, 2, 3, 4, 5]
print(f"append: {a}")
print(f"extend: {b}")


# ── SECTION 4: remove() — Remove by VALUE ─────────────────────

numbers = [10, 20, 30, 40, 20, 50]
numbers.remove(20)
# removes the FIRST occurrence of 20 only
print(numbers)
# [10, 30, 40, 20, 50]  ← second 20 still there!

# numbers.remove(99)  ← ❌ CRASHES if value not found: ValueError


# ── SECTION 5: pop() — Remove by INDEX ────────────────────────

colors = ["red", "green", "blue", "yellow"]

popped = colors.pop()
# pop() with NO argument removes and RETURNS the LAST item
print(f"Popped: {popped}")
print(f"List  : {colors}")

popped2 = colors.pop(1)
# pop(index) removes and RETURNS the item at that index
print(f"Popped: {popped2}")
print(f"List  : {colors}")


# ── SECTION 6: clear() — Remove ALL items ─────────────────────

temp = [1, 2, 3, 4, 5]
print(f"Before clear: {temp}")
temp.clear()
print(f"After clear : {temp}")
# [] ← empty list, but the variable still EXISTS


# ── SECTION 7: index() — Find position of a value ─────────────

animals = ["cat", "dog", "bird", "dog", "fish"]
print(animals.index("dog"))
# 1 ← returns index of the FIRST occurrence
# animals.index("lion")  ← ❌ CRASHES if not found


# ── SECTION 8: count() — Count occurrences ────────────────────

nums = [1, 2, 3, 2, 4, 2, 5]
print(nums.count(2))     # 3 ← appears three times
print(nums.count(9))     # 0 ← not there, returns 0 (no crash!)


# ── SECTION 9: sort() — Sort IN PLACE ─────────────────────────

scores = [85, 42, 91, 67, 23, 78]
scores.sort()
print(f"Ascending : {scores}")

scores.sort(reverse=True)
print(f"Descending: {scores}")

words = ["banana", "apple", "mango", "cherry"]
words.sort()
print(f"Alphabetical: {words}")

words.sort(reverse=True)
print(f"Reverse alpha: {words}")

# IMPORTANT: sort() changes the original list and returns None
# sorted() (Section 11) creates a NEW list instead


# ── SECTION 10: reverse() — Reverse IN PLACE ──────────────────

items = [1, 2, 3, 4, 5]
items.reverse()
print(f"Reversed: {items}")
# [5, 4, 3, 2, 1]


# ── SECTION 11: sorted() and reversed() — Non-destructive ──────

original = [5, 2, 8, 1, 9, 3]
sorted_copy = sorted(original)
print(f"Original     : {original}")
print(f"Sorted copy  : {sorted_copy}")
# original is UNCHANGED — sorted() creates a brand new list

sorted_desc = sorted(original, reverse=True)
print(f"Sorted desc  : {sorted_desc}")


# ── SECTION 12: copy() — Make a safe copy ─────────────────────

list1 = [1, 2, 3, 4, 5]
list2 = list1           # ⚠️ NOT a copy! Both point to the SAME list
list3 = list1.copy()    # ✅ A real independent copy

list2.append(99)
print(f"list1 (original): {list1}")   # also changed! ← the trap
print(f"list2 (alias)   : {list2}")
print(f"list3 (copy)    : {list3}")   # safely unaffected


# ── SECTION 13: Practical — To-Do List App ────────────────────

def show_todos(todos):
    if not todos:
        print("  No tasks yet!")
        return
    for i, task in enumerate(todos, start=1):
        print(f"  {i}. {task}")

print("\n--- Simple To-Do List ---")
todo_list = []

while True:
    print("\n1.Add  2.Done(remove)  3.View  4.Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            todo_list.append(task)
            print(f"  Added: '{task}'")
    elif choice == "2":
        show_todos(todo_list)
        if todo_list:
            try:
                num = int(input("Enter task number to mark done: "))
                if 1 <= num <= len(todo_list):
                    done = todo_list.pop(num - 1)
                    print(f"  Removed: '{done}'")
                else:
                    print("  Invalid number!")
            except ValueError:
                print("  Enter a valid number!")
    elif choice == "3":
        print("\nYour Tasks:")
        show_todos(todo_list)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("  Invalid choice!")

# ============================================================
# END OF DAY 22
# ============================================================