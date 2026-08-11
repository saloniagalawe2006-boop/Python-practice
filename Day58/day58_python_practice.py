"""
🐍 Day 58: Dataclasses
"""

from dataclasses import dataclass, field

# ----------------------------------------------------
# 1. The OLD way — a regular class for simple data storage
# ----------------------------------------------------

class StudentOld:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"StudentOld(name={self.name!r}, age={self.age}, score={self.score})"

    def __eq__(self, other):
        return (self.name, self.age, self.score) == (other.name, other.age, other.score)

s1 = StudentOld("Rahul", 22, 90)
print("Old-style class:", s1)


# ----------------------------------------------------
# 2. The NEW way — @dataclass writes all that boilerplate for you
# ----------------------------------------------------

@dataclass
class Student:
    name: str
    age: int
    score: float

s2 = Student("Priya", 21, 85.5)
print("\nDataclass:", s2)          # auto-generated __repr__


# ----------------------------------------------------
# 3. Dataclasses auto-generate __eq__ (value comparison)
# ----------------------------------------------------

s3 = Student("Priya", 21, 85.5)
s4 = Student("Anjali", 23, 95.0)

print("\ns2 == s3 (same values):", s2 == s3)
print("s2 == s4 (different values):", s2 == s4)


# ----------------------------------------------------
# 4. Default values
# ----------------------------------------------------

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True     # default value
    quantity: int = 0

p1 = Product("Laptop", 55000)
p2 = Product("Mouse", 500, quantity=10)

print("\n--- Default values ---")
print(p1)
print(p2)


# ----------------------------------------------------
# 5. Using field() for mutable defaults (lists, dicts)
# ----------------------------------------------------
# You CANNOT do: tags: list = []  directly (shared mutable default bug)
# Use field(default_factory=list) instead

@dataclass
class Article:
    title: str
    tags: list = field(default_factory=list)

a1 = Article("Python Basics")
a1.tags.append("python")
a1.tags.append("beginner")

a2 = Article("Advanced Python")   # gets its OWN empty list, not shared!

print("\n--- Mutable defaults with field() ---")
print(a1)
print(a2)


# ----------------------------------------------------
# 6. Adding methods to a dataclass (just like a normal class)
# ----------------------------------------------------

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print("\n--- Dataclass with methods ---")
print(f"Rectangle: {rect}")
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")


# ----------------------------------------------------
# 7. Making a dataclass immutable (like a tuple/namedtuple)
# ----------------------------------------------------

@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(3, 4)
print("\n--- Frozen (immutable) dataclass ---")
print(point)

try:
    point.x = 100
except Exception as e:
    print("Error:", e)


# ----------------------------------------------------
# 8. Comparing values with order=True (enables <, >, etc.)
# ----------------------------------------------------

@dataclass(order=True)
class Score:
    value: int

scores = [Score(90), Score(45), Score(88)]
print("\n--- Sortable dataclass ---")
print("Sorted scores:", sorted(scores))


"""
📝 Quick Recap:
- @dataclass automatically generates __init__, __repr__, __eq__
- Type hints (name: str) declare the fields
- Default values: field: type = default_value
- field(default_factory=list/dict) -> safe way to set mutable defaults
- @dataclass(frozen=True) -> makes instances immutable
- @dataclass(order=True)  -> enables <, >, sorting between instances
- Dataclasses are perfect for simple data-holding classes:
  records, configs, coordinates, DTOs (data transfer objects)
"""