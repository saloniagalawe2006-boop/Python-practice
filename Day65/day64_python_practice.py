"""
🐍 Day 65: Magic Methods (Dunder Methods)
"""

# ----------------------------------------------------
# 1. What are Magic Methods?
# ----------------------------------------------------
# Methods surrounded by double underscores (__method__)
# that let your custom objects work with Python's built-in
# syntax: print(), +, ==, len(), [] indexing, and more.
# "Dunder" = Double UNDERscore.


# ----------------------------------------------------
# 2. __init__ and __str__ (you already know these!)
# ----------------------------------------------------

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # controls what print(obj) and str(obj) show
        return f"'{self.title}' ({self.pages} pages)"

    def __repr__(self):
        # controls what you see in the console / debugger / lists
        return f"Book(title={self.title!r}, pages={self.pages})"

b1 = Book("Atomic Habits", 320)
print("--- __str__ and __repr__ ---")
print(b1)            # uses __str__
print(str(b1))        # uses __str__
print(repr(b1))        # uses __repr__
print([b1])            # lists use __repr__ for their items


# ----------------------------------------------------
# 3. __len__ -> makes len(obj) work
# ----------------------------------------------------

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

pl = Playlist(["Song A", "Song B", "Song C"])
print("\n--- __len__ ---")
print("Number of songs:", len(pl))


# ----------------------------------------------------
# 4. __eq__, __lt__, __gt__ -> comparison operators
# ----------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __repr__(self):
        return f"{self.name}(${self.price})"

p1 = Product("Book", 300)
p2 = Product("Pen", 20)
p3 = Product("Bag", 300)

print("\n--- Comparison magic methods ---")
print("p1 == p3:", p1 == p3)
print("p1 > p2:", p1 > p2)
print("Sorted by price:", sorted([p1, p2, p3]))


# ----------------------------------------------------
# 5. __getitem__ and __setitem__ -> makes obj[index] work
# ----------------------------------------------------

class Roster:
    def __init__(self):
        self.students = {}

    def __setitem__(self, roll_no, name):
        self.students[roll_no] = name

    def __getitem__(self, roll_no):
        return self.students.get(roll_no, "Not found")

roster = Roster()
roster[1] = "Rahul"      # uses __setitem__
roster[2] = "Priya"

print("\n--- __getitem__/__setitem__ ---")
print("Roll 1:", roster[1])   # uses __getitem__
print("Roll 5:", roster[5])


# ----------------------------------------------------
# 6. __add__, __sub__ -> operator overloading (recap from Day 41)
# ----------------------------------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 1)
print("\n--- __add__/__sub__ ---")
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)


# ----------------------------------------------------
# 7. __contains__ -> makes 'in' keyword work
# ----------------------------------------------------

class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, name):
        return name in self.members

team = Team(["Rahul", "Priya", "Anjali"])
print("\n--- __contains__ ---")
print("Is Rahul in team?", "Rahul" in team)
print("Is Vikram in team?", "Vikram" in team)


# ----------------------------------------------------
# 8. __call__ -> makes an object CALLABLE like a function
# ----------------------------------------------------

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print("\n--- __call__ ---")
print("double(5):", double(5))
print("triple(5):", triple(5))


"""
📝 Quick Recap:
- __init__      -> constructor (runs on object creation)
- __str__       -> readable string for print()/str()
- __repr__      -> unambiguous string for debugging/console
- __len__       -> makes len(obj) work
- __eq__, __lt__, __gt__ -> enables ==, <, >, sorted(), etc.
- __getitem__/__setitem__ -> makes obj[key] read/write work
- __add__, __sub__, etc.  -> operator overloading (+, -, *, /)
- __contains__  -> enables the 'in' keyword
- __call__      -> makes an object callable like obj(args)
- Magic methods let custom classes integrate naturally with
  Python's built-in syntax and functions
"""