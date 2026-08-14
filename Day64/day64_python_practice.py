"""
🐍 Day 64: Enums (enum module)
"""

from enum import Enum, auto, IntEnum

# ----------------------------------------------------
# 1. What is an Enum?
# ----------------------------------------------------
# An Enum groups a set of NAMED CONSTANTS together,
# making code more readable and preventing "magic values"
# (like using raw strings/numbers scattered everywhere).


# ----------------------------------------------------
# 2. The old way — using plain constants (error-prone)
# ----------------------------------------------------

STATUS_PENDING = "pending"
STATUS_APPROVED = "approved"
STATUS_REJECTED = "rejected"

order_status = STATUS_APPROVED
print("Old way:", order_status)
# Problem: nothing stops you from typing "aproved" (typo) by mistake!


# ----------------------------------------------------
# 3. The Enum way — safer, grouped, self-documenting
# ----------------------------------------------------

class OrderStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

status = OrderStatus.APPROVED
print("\n--- Basic Enum ---")
print("Status:", status)
print("Name:", status.name)
print("Value:", status.value)


# ----------------------------------------------------
# 4. Comparing enum members
# ----------------------------------------------------

print("\n--- Comparisons ---")
print("Is approved?", status == OrderStatus.APPROVED)
print("Is pending?", status == OrderStatus.PENDING)


# ----------------------------------------------------
# 5. Using auto() -> Python assigns values automatically
# ----------------------------------------------------

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print("\n--- auto() ---")
for color in Color:
    print(color.name, "=", color.value)


# ----------------------------------------------------
# 6. Looping through all members of an Enum
# ----------------------------------------------------

print("\n--- Looping through OrderStatus ---")
for s in OrderStatus:
    print(f"{s.name}: {s.value}")


# ----------------------------------------------------
# 7. Accessing enum members by name or value
# ----------------------------------------------------

print("\n--- Accessing members ---")
by_name = OrderStatus["REJECTED"]
by_value = OrderStatus("pending")

print("By name:", by_name)
print("By value:", by_value)


# ----------------------------------------------------
# 8. IntEnum -> behaves like an int (supports comparisons like <, >)
# ----------------------------------------------------

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print("\n--- IntEnum ---")
print("HIGH > LOW?", Priority.HIGH > Priority.LOW)
print("MEDIUM + 1 =", Priority.MEDIUM + 1)   # works because it IS an int


# ----------------------------------------------------
# 9. Real-world example: a Task with a status enum
# ----------------------------------------------------

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    def __init__(self, title, status=TaskStatus.TODO):
        self.title = title
        self.status = status

    def mark_done(self):
        self.status = TaskStatus.DONE

    def __str__(self):
        return f"{self.title} [{self.status.value}]"

print("\n--- Task with Enum status ---")
task = Task("Finish Day 64")
print(task)
task.mark_done()
print(task)


# ----------------------------------------------------
# 10. Using Enum in conditional logic
# ----------------------------------------------------

def handle_order(order_status: OrderStatus):
    if order_status == OrderStatus.PENDING:
        print("Order is being processed...")
    elif order_status == OrderStatus.APPROVED:
        print("Order approved! Preparing shipment.")
    elif order_status == OrderStatus.REJECTED:
        print("Order was rejected.")

print("\n--- Using Enum in logic ---")
handle_order(OrderStatus.APPROVED)
handle_order(OrderStatus.REJECTED)


"""
📝 Quick Recap:
- from enum import Enum, auto, IntEnum
- class Name(Enum): MEMBER = value   -> groups related constants
- .name  -> the member's name (string)
- .value -> the member's assigned value
- auto() -> automatically assigns increasing values (1, 2, 3...)
- EnumClass["NAME"] / EnumClass(value) -> lookup a member
- IntEnum -> enum that also behaves like a real integer
- Enums prevent typos, improve readability, and are self-documenting
  compared to raw strings/numbers scattered through code
"""