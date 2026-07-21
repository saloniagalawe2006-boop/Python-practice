"""
🐍 Day 39: OOP — Inheritance
"""

# ----------------------------------------------------
# 1. What is Inheritance?
# ----------------------------------------------------
# Inheritance lets a class (child) REUSE code from
# another class (parent), instead of rewriting it.
#
# Real-life analogy: "Animal" is a parent class.
# "Dog" and "Cat" are child classes that inherit common
# traits (like eating, sleeping) but also have their own.


# ----------------------------------------------------
# 2. Basic inheritance
# ----------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):     # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Tommy")
dog1.eat()      # inherited from Animal
dog1.sleep()    # inherited from Animal
dog1.bark()     # defined in Dog itself


# ----------------------------------------------------
# 3. Overriding a parent method
# ----------------------------------------------------

class Cat(Animal):
    def eat(self):   # overrides Animal's eat()
        print(f"{self.name} eats fish quietly.")

cat1 = Cat("Whiskers")
cat1.eat()      # uses Cat's own version
cat1.sleep()    # still inherited from Animal


# ----------------------------------------------------
# 4. Using super() to call the parent's method/constructor
# ----------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # call parent's __init__
        self.team_size = team_size

    def show_info(self):
        super().show_info()               # call parent's method too
        print(f"Team size: {self.team_size}")

print("\n--- super() demo ---")
mgr = Manager("Anjali", 80000, 5)
mgr.show_info()


# ----------------------------------------------------
# 5. Multi-level inheritance
# ----------------------------------------------------

class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class SportsCar(Car):
    def turbo_boost(self):
        print("Turbo boost activated! 🚀")

print("\n--- Multi-level inheritance ---")
sc = SportsCar()
sc.start()          # from Vehicle
sc.drive()          # from Car
sc.turbo_boost()    # from SportsCar


# ----------------------------------------------------
# 6. Checking inheritance relationships
# ----------------------------------------------------

print("\nIs sc an instance of Car?", isinstance(sc, Car))
print("Is sc an instance of Vehicle?", isinstance(sc, Vehicle))
print("Is SportsCar a subclass of Vehicle?", issubclass(SportsCar, Vehicle))


# ----------------------------------------------------
# 7. Real-world example: different employee types
# ----------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I am in grade {self.grade}.")

print("\n--- Real-world example ---")
t = Teacher("Mr. Sharma", "Mathematics")
s = Student("Rahul", 10)

t.introduce()
s.introduce()


"""
📝 Quick Recap:
- class Child(Parent):        -> Child inherits from Parent
- Child gets ALL of Parent's attributes and methods for free
- Overriding: redefine a method in the child with the same name
- super().__init__(...)       -> calls the parent's constructor
- super().method_name()       -> calls the parent's version of a method
- isinstance(obj, Class)      -> checks if obj belongs to Class
- issubclass(Child, Parent)   -> checks class relationship
- Inheritance = code reuse + building specialized versions of a class
"""