"""
🐍 Day 40: OOP — Encapsulation
"""

# ----------------------------------------------------
# 1. What is Encapsulation?
# ----------------------------------------------------
# Encapsulation means BUNDLING data (attributes) and methods
# together, while RESTRICTING direct access to some of it —
# protecting internal details from being changed carelessly.
#
# Python uses naming conventions to indicate access level:
#   public     -> name        (accessible from anywhere)
#   protected  -> _name       (convention: internal use only)
#   private    -> __name      (name-mangled, harder to access)


# ----------------------------------------------------
# 2. Public attributes (default, no restriction)
# ----------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name   # public
        self.age = age      # public

s1 = Student("Rahul", 22)
print("Public access:", s1.name, s1.age)
s1.age = 23   # can be changed freely from outside
print("After direct change:", s1.age)


# ----------------------------------------------------
# 3. Protected attributes (single underscore _name)
# ----------------------------------------------------
# Convention only -> still accessible, but signals
# "please treat this as internal, don't touch directly"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # protected

    def show_salary(self):
        print(f"{self.name}'s salary: {self._salary}")

emp = Employee("Priya", 50000)
emp.show_salary()
print("Still technically accessible:", emp._salary)   # works, but discouraged


# ----------------------------------------------------
# 4. Private attributes (double underscore __name)
# ----------------------------------------------------
# Name-mangled by Python -> much harder to access directly from outside

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("Anjali", 1000)
account.deposit(500)
print("\nBalance via method:", account.get_balance())

print("\n--- Trying direct access ---")
try:
    print(account.__balance)
except AttributeError as e:
    print("Error:", e)


# ----------------------------------------------------
# 5. Using getters and setters (controlled access)
# ----------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = new_price

product = Product("Laptop", 50000)
print("\nOriginal price:", product.get_price())

product.set_price(45000)
print("Updated price:", product.get_price())

product.set_price(-100)   # invalid -> rejected safely


# ----------------------------------------------------
# 6. Using @property for cleaner getter/setter syntax
# ----------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):          # acts like a read-only-looking attribute
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            print("Radius must be positive!")
        else:
            self.__radius = value

    @property
    def area(self):
        return 3.14159 * self.__radius ** 2

print("\n--- @property demo ---")
c = Circle(5)
print("Radius:", c.radius)        # looks like a normal attribute
print("Area:", round(c.area, 2))

c.radius = 10                     # uses the setter, validated
print("Updated radius:", c.radius)
print("Updated area:", round(c.area, 2))

c.radius = -5                     # rejected by setter


"""
📝 Quick Recap:
- Public     : self.name       -> accessible from anywhere
- Protected  : self._name      -> convention, "internal use" signal only
- Private    : self.__name     -> name-mangled, not directly accessible
- Getters/Setters -> controlled, validated access to private data
- @property / @x.setter -> lets private data be accessed like a
  normal attribute, while still running validation behind the scenes
- Encapsulation protects data integrity and hides implementation details
"""