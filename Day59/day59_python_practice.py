"""
🐍 Day 59: Type Hints (typing module)
"""

from typing import List, Dict, Tuple, Optional, Union, Callable, Any

# ----------------------------------------------------
# 1. What are Type Hints?
# ----------------------------------------------------
# Python is dynamically typed (you don't declare types).
# Type hints let you ANNOTATE what type a variable/function
# SHOULD be, for readability and tooling support — but Python
# does NOT enforce them at runtime (they're just hints/docs).


# ----------------------------------------------------
# 2. Basic variable type hints
# ----------------------------------------------------

name: str = "Rahul"
age: int = 22
gpa: float = 8.5
is_active: bool = True

print(name, age, gpa, is_active)


# ----------------------------------------------------
# 3. Function parameter and return type hints
# ----------------------------------------------------

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

print("\nadd(3, 5):", add(3, 5))
print(greet("Priya"))


# ----------------------------------------------------
# 4. Type hints DON'T stop you from passing wrong types
# ----------------------------------------------------
# Python won't crash here -> hints are for humans/tools, not enforcement

print("\n--- Hints are not enforced at runtime ---")
result = add("3", "5")   # works because + also works on strings!
print("add('3', '5') =", result)


# ----------------------------------------------------
# 5. Collection type hints -> List, Dict, Tuple
# ----------------------------------------------------

def get_names() -> List[str]:
    return ["Rahul", "Priya", "Anjali"]

def get_scores() -> Dict[str, int]:
    return {"Rahul": 90, "Priya": 85}

def get_coordinates() -> Tuple[float, float]:
    return (12.34, 56.78)

print("\nNames:", get_names())
print("Scores:", get_scores())
print("Coordinates:", get_coordinates())


# ----------------------------------------------------
# 6. Optional -> value can be the type OR None
# ----------------------------------------------------

def find_student(student_id: int) -> Optional[str]:
    students = {1: "Rahul", 2: "Priya"}
    return students.get(student_id)   # returns None if not found

print("\nfind_student(1):", find_student(1))
print("find_student(99):", find_student(99))


# ----------------------------------------------------
# 7. Union -> value can be ONE of several types
# ----------------------------------------------------

def process_id(user_id: Union[int, str]) -> str:
    return f"Processing ID: {user_id}"

print("\n", process_id(101))
print(process_id("USR-101"))

# Python 3.10+ shorthand: int | str   (same meaning as Union[int, str])


# ----------------------------------------------------
# 8. Callable -> hinting a function passed as an argument
# ----------------------------------------------------

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

def multiply(x: int, y: int) -> int:
    return x * y

print("\napply_operation(4, 5, multiply):", apply_operation(4, 5, multiply))


# ----------------------------------------------------
# 9. Type hints for class attributes
# ----------------------------------------------------

class Student:
    name: str
    age: int
    scores: List[int]

    def __init__(self, name: str, age: int, scores: List[int]):
        self.name = name
        self.age = age
        self.scores = scores

    def average(self) -> float:
        return sum(self.scores) / len(self.scores)

s = Student("Anjali", 23, [90, 85, 95])
print("\nStudent average:", s.average())


# ----------------------------------------------------
# 10. Any -> when a type could truly be anything
# ----------------------------------------------------

def print_value(value: Any) -> None:
    print("Value:", value)

print()
print_value(42)
print_value("hello")
print_value([1, 2, 3])


"""
📝 Quick Recap:
- name: type = value            -> variable type hint
- def f(x: int) -> str:         -> parameter and return type hints
- Type hints are NOT enforced at runtime — they're documentation
  and tooling support (IDEs, linters like mypy catch mismatches)
- List[X], Dict[K, V], Tuple[X, Y] -> typed collections
- Optional[X]  == Union[X, None] -> value might be None
- Union[X, Y]  -> value could be X OR Y
- Callable[[ArgTypes], ReturnType] -> hint for function arguments
- Any -> explicitly says "could be any type"
- Type hints make large codebases easier to read, understand, and debug
"""