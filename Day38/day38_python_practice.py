"""
🐍 Day 38: OOP — Classes & Objects (Basics)
"""

# ----------------------------------------------------
# 1. What is a Class?
# ----------------------------------------------------
# A class is a BLUEPRINT for creating objects.
# An object is a specific INSTANCE made from that blueprint.
#
# Real-life analogy: "Student" is a class (the blueprint),
# "Rahul" and "Priya" are objects (actual students built from it).


# ----------------------------------------------------
# 2. Creating a simple class
# ----------------------------------------------------

class Student:
    pass   # empty class for now

s1 = Student()   # creating an object (instance)
print("s1 is:", s1)
print("Type:", type(s1))


# ----------------------------------------------------
# 3. The __init__ method (constructor)
# ----------------------------------------------------
# __init__ runs automatically when an object is created.
# 'self' refers to the object itself.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 22)
s2 = Student("Priya", 21)

print("\ns1 name:", s1.name, "| age:", s1.age)
print("s2 name:", s2.name, "| age:", s2.age)


# ----------------------------------------------------
# 4. Adding methods (functions inside a class)
# ----------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

s1 = Student("Rahul", 22)
s1.greet()


# ----------------------------------------------------
# 5. Instance attributes vs class attributes
# ----------------------------------------------------

class Student:
    school_name = "Python Academy"    # class attribute -> shared by ALL objects

    def __init__(self, name, age):
        self.name = name              # instance attribute -> unique per object
        self.age = age

s1 = Student("Rahul", 22)
s2 = Student("Priya", 21)

print("\ns1 school:", s1.school_name)
print("s2 school:", s2.school_name)
print("Both share the same class attribute:", s1.school_name == s2.school_name)


# ----------------------------------------------------
# 6. Modifying object attributes
# ----------------------------------------------------

s1.age = 23   # updating an instance attribute
print("\nUpdated s1 age:", s1.age)


# ----------------------------------------------------
# 7. A more complete example
# ----------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

print("\n--- BankAccount demo ---")
account = BankAccount("Anjali", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(5000)


# ----------------------------------------------------
# 8. Creating multiple independent objects
# ----------------------------------------------------

acc1 = BankAccount("Vikram", 500)
acc2 = BankAccount("Sneha", 2000)

acc1.deposit(100)
acc2.withdraw(500)

print("\nFinal balances:")
acc1.show_balance()
acc2.show_balance()


"""
📝 Quick Recap:
- class ClassName:          -> defines a blueprint
- __init__(self, ...)       -> runs automatically on object creation
- self                      -> refers to the current object
- Instance attributes       -> unique to each object (self.x = x)
- Class attributes          -> shared across ALL objects of the class
- Methods                   -> functions defined inside a class
- object = ClassName(args)  -> creates a new object (instance)
"""