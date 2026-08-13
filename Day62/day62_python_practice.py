"""
🐍 Day 62: The collections Module
Counter, defaultdict, namedtuple, deque, OrderedDict
"""

from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

# ----------------------------------------------------
# 1. Counter -> counts occurrences automatically
# ----------------------------------------------------

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)

print("--- Counter ---")
print("Word counts:", word_counts)
print("Most common 2:", word_counts.most_common(2))
print("Count of 'apple':", word_counts["apple"])
print("Count of missing word:", word_counts["mango"])   # 0, no KeyError!

# Counter also works on strings
letter_counts = Counter("mississippi")
print("Letter counts:", letter_counts)


# ----------------------------------------------------
# 2. defaultdict -> dict with automatic default values
# ----------------------------------------------------
# Normal dict raises KeyError for missing keys.
# defaultdict AUTO-CREATES a default value instead.

print("\n--- defaultdict ---")

normal_dict = {}
try:
    normal_dict["fruits"].append("apple")
except KeyError as e:
    print("Normal dict error:", e)

grouped = defaultdict(list)          # missing keys default to an empty list
grouped["fruits"].append("apple")
grouped["fruits"].append("banana")
grouped["vegetables"].append("carrot")
print("Grouped data:", dict(grouped))

# Real-world example: grouping students by grade
students = [("Rahul", "A"), ("Priya", "B"), ("Anjali", "A"), ("Vikram", "C")]
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)
print("Students by grade:", dict(by_grade))


# ----------------------------------------------------
# 3. namedtuple -> tuple with NAMED fields (readable + immutable)
# ----------------------------------------------------

print("\n--- namedtuple ---")

Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)

print("Point:", p1)
print("Access by name:", p1.x, p1.y)
print("Access by index:", p1[0], p1[1])

Student = namedtuple("Student", ["name", "age", "score"])
s1 = Student("Rahul", 22, 90)
print("Student:", s1)
print("Student name:", s1.name)


# ----------------------------------------------------
# 4. deque -> fast additions/removals from BOTH ends
# ----------------------------------------------------
# Regular lists are slow for insert/remove at the FRONT.
# deque (double-ended queue) is optimized for that.

print("\n--- deque ---")

queue = deque(["Rahul", "Priya", "Anjali"])
queue.append("Vikram")          # add to the right (end)
queue.appendleft("Sneha")       # add to the left (start)
print("After appends:", queue)

queue.pop()                     # remove from the right
queue.popleft()                 # remove from the left
print("After pops:", queue)

# deque with a max length -> acts like a rolling window
recent_actions = deque(maxlen=3)
for action in ["login", "click", "scroll", "purchase", "logout"]:
    recent_actions.append(action)
    print("Recent actions:", list(recent_actions))


# ----------------------------------------------------
# 5. OrderedDict -> preserves insertion order (mostly historical)
# ----------------------------------------------------
# Note: regular dicts in Python 3.7+ ALSO preserve insertion order,
# but OrderedDict has some extra methods like move_to_end().

print("\n--- OrderedDict ---")

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print("OrderedDict:", od)

od.move_to_end("first")   # moves 'first' to the end
print("After move_to_end('first'):", od)


# ----------------------------------------------------
# 6. Real-world example: analyzing website visit logs
# ----------------------------------------------------

visits = ["home", "products", "home", "cart", "checkout", "home", "products"]

visit_counts = Counter(visits)
print("\n--- Website visit analysis ---")
print("Page visit counts:", visit_counts)
print("Top 2 most visited pages:", visit_counts.most_common(2))


"""
📝 Quick Recap:
- Counter(iterable)      -> counts item frequencies, has most_common()
- defaultdict(type)      -> auto-creates missing keys with a default
- namedtuple("Name", [fields]) -> tuple with readable named fields
- deque(iterable, maxlen=n)    -> fast append/pop from BOTH ends
- OrderedDict()           -> dict that remembers insertion order
  (regular dicts do this too since Python 3.7, but OrderedDict
  adds extras like move_to_end())
- These are memory/speed-efficient alternatives to plain lists/dicts
  for specific, common data-handling patterns
"""