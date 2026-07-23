"""
🐍 Day 42: OOP — Abstraction
"""

# ----------------------------------------------------
# 1. What is Abstraction?
# ----------------------------------------------------
# Abstraction means hiding COMPLEX implementation details
# and showing only the essential features to the user.
#
# Real-life analogy: When you drive a car, you use the
# steering wheel, brake, accelerator — you don't need to
# know how the engine internally works. The engine's
# complexity is "abstracted away".


# ----------------------------------------------------
# 2. Abstract classes using the 'abc' module
# ----------------------------------------------------
# An abstract class CANNOT be instantiated directly.
# It defines methods that MUST be implemented by any
# child class — enforcing a consistent structure.

from abc import ABC, abstractmethod

class Shape(ABC):          # ABC = Abstract Base Class
    @abstractmethod
    def area(self):
        pass                # no implementation here -> forces child to define it

    @abstractmethod
    def perimeter(self):
        pass


# ----------------------------------------------------
# 3. Trying to instantiate an abstract class directly
# ----------------------------------------------------

print("--- Trying to create Shape() directly ---")
try:
    s = Shape()
except TypeError as e:
    print("Error:", e)


# ----------------------------------------------------
# 4. Child classes MUST implement all abstract methods
# ----------------------------------------------------

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

print("\n--- Concrete shapes ---")
rect = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle -> area: {rect.area()}, perimeter: {rect.perimeter()}")
print(f"Circle    -> area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")


# ----------------------------------------------------
# 5. What happens if a child forgets to implement a method?
# ----------------------------------------------------

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    # perimeter() is MISSING on purpose

print("\n--- Incomplete child class ---")
try:
    t = Triangle(6, 4)
except TypeError as e:
    print("Error:", e)


# ----------------------------------------------------
# 6. Abstraction enforces a common interface
# ----------------------------------------------------
# Every shape GUARANTEES an .area() and .perimeter() method,
# so we can safely loop over any mix of shapes.

shapes = [Rectangle(2, 3), Circle(5)]

print("\n--- Common interface in action ---")
for shape in shapes:
    print(f"{type(shape).__name__}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")


# ----------------------------------------------------
# 7. Real-world example: payment system interface
# ----------------------------------------------------

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

class Wallet(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Wallet balance.")

def checkout(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)   # doesn't care HOW payment happens internally

print("\n--- Payment system demo ---")
checkout(CreditCard(), 1500)
checkout(UPI(), 500)
checkout(Wallet(), 200)


"""
📝 Quick Recap:
- Abstraction hides complex details, exposes only what's needed
- from abc import ABC, abstractmethod
- class Name(ABC):          -> makes a class abstract
- @abstractmethod           -> forces child classes to implement it
- Abstract classes CANNOT be instantiated directly
- Child classes MUST implement every abstract method, or they
  ALSO become abstract (can't be instantiated)
- Abstraction + Polymorphism together let you build flexible,
  consistent systems (e.g., different shapes, payment methods, etc.)
"""