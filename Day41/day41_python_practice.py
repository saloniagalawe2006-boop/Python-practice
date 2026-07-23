"""
🐍 Day 41: OOP — Polymorphism
"""

# ----------------------------------------------------
# 1. What is Polymorphism?
# ----------------------------------------------------
# "Poly" = many, "morph" = forms.
# Polymorphism means the SAME method name behaves
# DIFFERENTLY depending on which object calls it.


# ----------------------------------------------------
# 2. Polymorphism with different classes (method overriding)
# ----------------------------------------------------

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks: Woof!")

class Cat(Animal):
    def speak(self):
        print("The cat meows: Meow!")

class Cow(Animal):
    def speak(self):
        print("The cow moos: Moo!")

animals = [Dog(), Cat(), Cow(), Animal()]

print("--- Same method, different behavior ---")
for animal in animals:
    animal.speak()   # calls the RIGHT version automatically


# ----------------------------------------------------
# 2b. This is the core idea: one interface, many forms
# ----------------------------------------------------
# We didn't need to check "if it's a Dog, do this... if Cat, do that..."
# Python figures out the correct .speak() automatically.


# ----------------------------------------------------
# 3. Polymorphism with built-in functions
# ----------------------------------------------------
# len() behaves differently depending on the data type

print("\n--- Polymorphism with len() ---")
print("len of string:", len("Python"))
print("len of list:", len([1, 2, 3, 4]))
print("len of dict:", len({"a": 1, "b": 2}))


# ----------------------------------------------------
# 4. Polymorphism with operators (operator overloading)
# ----------------------------------------------------
# The '+' operator behaves differently for different types

print("\n--- Polymorphism with + operator ---")
print("Numbers:", 5 + 3)
print("Strings:", "Hello " + "World")
print("Lists:", [1, 2] + [3, 4])


# ----------------------------------------------------
# 5. Custom operator overloading using __add__
# ----------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):        # defines what '+' means for Points
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):               # defines what print() shows
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2   # uses our custom __add__

print("\n--- Custom operator overloading ---")
print("p1:", p1)
print("p2:", p2)
print("p1 + p2 =", p3)


# ----------------------------------------------------
# 6. Polymorphism with function arguments (duck typing)
# ----------------------------------------------------
# "If it walks like a duck and quacks like a duck, treat it like a duck."
# Python doesn't care about the exact type — only that the
# object supports the method being called.

class Bird:
    def move(self):
        print("The bird flies.")

class Fish:
    def move(self):
        print("The fish swims.")

def make_it_move(creature):
    creature.move()   # works for ANY object with a .move() method

print("\n--- Duck typing ---")
make_it_move(Bird())
make_it_move(Fish())


# ----------------------------------------------------
# 7. Real-world example: shape area calculator
# ----------------------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 4)]

print("\n--- Shape area calculator ---")
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")


"""
📝 Quick Recap:
- Polymorphism = same method/operator name, different behavior
- Method overriding: child classes redefine a parent's method
- Built-in functions like len(), + also behave polymorphically
- __add__, __str__, etc. let YOU define custom operator behavior
- Duck typing: Python cares about available methods, not exact type
- Polymorphism makes code flexible — loop over different objects
  and call the same method name without checking types manually
"""