"""
🐍 Day 44: Iterators & Generators
"""

# ----------------------------------------------------
# 1. What is an Iterable vs Iterator?
# ----------------------------------------------------
# Iterable : anything you can loop over (list, string, tuple, dict...)
# Iterator : an object that produces items ONE AT A TIME using next()

my_list = [1, 2, 3]
my_iterator = iter(my_list)   # get an iterator from an iterable

print("Using next() manually:")
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print("\n--- Calling next() after exhausting the iterator ---")
try:
    print(next(my_iterator))
except StopIteration:
    print("Error: StopIteration - no more items!")


# ----------------------------------------------------
# 2. How a 'for' loop actually works behind the scenes
# ----------------------------------------------------
# for item in my_list:  is basically doing this internally:

iterator = iter(my_list)
print("\n--- Manual for-loop simulation ---")
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break


# ----------------------------------------------------
# 3. What is a Generator?
# ----------------------------------------------------
# A generator is a special function that YIELDS values
# one at a time, instead of returning them all at once.
# It remembers where it left off between calls.

def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n     # pauses here, remembers state, resumes on next call
        n += 1

print("\n--- Basic generator ---")
counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))

print("\nLooping through remaining values:")
for value in counter:   # continues from where it left off
    print(value)


# ----------------------------------------------------
# 4. Why use generators? (Memory efficiency)
# ----------------------------------------------------
# A list stores ALL values in memory at once.
# A generator produces values ONE AT A TIME -> saves memory,
# especially useful for huge or infinite sequences.

def squares_list(n):
    return [i * i for i in range(n)]      # builds the WHOLE list in memory

def squares_generator(n):
    for i in range(n):
        yield i * i                        # produces one value at a time

print("\n--- List vs Generator ---")
print("List version:", squares_list(5))
print("Generator version:", list(squares_generator(5)))   # convert to see all


# ----------------------------------------------------
# 5. Generator expressions (like list comprehension, but lazy)
# ----------------------------------------------------

gen_expr = (i * i for i in range(5))    # notice: () instead of []
print("\nGenerator expression object:", gen_expr)
print("Values:", list(gen_expr))


# ----------------------------------------------------
# 6. Real-world example: reading large files lazily
# ----------------------------------------------------
# Instead of loading an entire huge file into memory,
# a generator can process it line-by-line efficiently.

def read_large_data(data_lines):
    for line in data_lines:
        yield line.strip().upper()

fake_file_lines = ["hello\n", "world\n", "python\n"]

print("\n--- Lazy line processing ---")
for processed_line in read_large_data(fake_file_lines):
    print(processed_line)


# ----------------------------------------------------
# 7. Infinite generator (only possible because it's LAZY)
# ----------------------------------------------------

def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1

print("\n--- Infinite generator (taking only first 5) ---")
gen = infinite_counter()
for _ in range(5):
    print(next(gen))


"""
📝 Quick Recap:
- iter(obj)      -> gets an iterator from an iterable
- next(iterator) -> gets the next value; raises StopIteration when done
- 'for' loops use iter() and next() automatically behind the scenes
- def with 'yield' -> creates a generator function
- Generators produce values LAZILY (one at a time), saving memory
- Generator expression: (expr for item in iterable) -> lazy version
  of a list comprehension
- Great for: huge datasets, infinite sequences, streaming file reads
"""