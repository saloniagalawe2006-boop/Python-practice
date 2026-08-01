"""
🐍 Day 51: The itertools Module
"""

import itertools

# ----------------------------------------------------
# 1. What is itertools?
# ----------------------------------------------------
# A built-in module full of fast, memory-efficient tools
# for working with iterators — combinations, permutations,
# infinite sequences, grouping, chaining, and more.


# ----------------------------------------------------
# 2. itertools.count() -> infinite counter
# ----------------------------------------------------

print("--- count() ---")
counter = itertools.count(start=1, step=2)   # 1, 3, 5, 7, ...
for _ in range(5):
    print(next(counter))


# ----------------------------------------------------
# 3. itertools.cycle() -> repeat a sequence forever
# ----------------------------------------------------

print("\n--- cycle() ---")
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(colors))


# ----------------------------------------------------
# 4. itertools.repeat() -> repeat a value N times
# ----------------------------------------------------

print("\n--- repeat() ---")
repeated = list(itertools.repeat("Python", 4))
print(repeated)


# ----------------------------------------------------
# 5. itertools.chain() -> combine multiple iterables into one
# ----------------------------------------------------

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined = list(itertools.chain(list1, list2))
print("\n--- chain() ---")
print(combined)


# ----------------------------------------------------
# 6. itertools.combinations() -> all possible groupings (order doesn't matter)
# ----------------------------------------------------

items = ["A", "B", "C"]
combos = list(itertools.combinations(items, 2))
print("\n--- combinations() (pick 2, order doesn't matter) ---")
print(combos)


# ----------------------------------------------------
# 7. itertools.permutations() -> all possible orderings (order matters)
# ----------------------------------------------------

perms = list(itertools.permutations(items, 2))
print("\n--- permutations() (pick 2, order matters) ---")
print(perms)


# ----------------------------------------------------
# 8. itertools.product() -> cartesian product (like nested loops)
# ----------------------------------------------------

sizes = ["S", "M", "L"]
colors_list = ["Red", "Blue"]
combos_product = list(itertools.product(sizes, colors_list))
print("\n--- product() (all size-color combos) ---")
print(combos_product)


# ----------------------------------------------------
# 9. itertools.groupby() -> group consecutive matching items
# ----------------------------------------------------

scores = [("Rahul", "Pass"), ("Priya", "Pass"), ("Vikram", "Fail"), ("Anjali", "Pass")]
scores_sorted = sorted(scores, key=lambda s: s[1])   # groupby needs sorted data

print("\n--- groupby() ---")
for status, group in itertools.groupby(scores_sorted, key=lambda s: s[1]):
    names = [name for name, _ in group]
    print(f"{status}: {names}")


# ----------------------------------------------------
# 10. Real-world example: generating unique team pairs
# ----------------------------------------------------

players = ["Rahul", "Priya", "Anjali", "Vikram"]
team_pairs = list(itertools.combinations(players, 2))

print("\n--- All possible 2-player teams ---")
for pair in team_pairs:
    print(pair)


# ----------------------------------------------------
# 11. itertools.islice() -> slice an iterator (works on infinite ones too!)
# ----------------------------------------------------

infinite_numbers = itertools.count(1)
first_five = list(itertools.islice(infinite_numbers, 5))
print("\n--- islice() on an infinite iterator ---")
print(first_five)


"""
📝 Quick Recap:
- count(start, step)   -> infinite counting sequence
- cycle(iterable)       -> repeats a sequence forever
- repeat(value, n)      -> repeats one value n times
- chain(iter1, iter2)   -> joins multiple iterables into one
- combinations(items, r)-> unordered groupings of size r
- permutations(items, r)-> ordered groupings of size r
- product(iter1, iter2) -> cartesian product (all combinations)
- groupby(iterable, key)-> groups CONSECUTIVE matching items
- islice(iterable, n)   -> takes a slice from any iterator
- Great for combinatorics, infinite streams, and efficient looping
"""