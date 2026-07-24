"""
🐍 Day 43: Mini Project — Library Management System (OOP)
Combines everything from Day 38-42:
Classes & Objects, Inheritance, Encapsulation,
Polymorphism, Abstraction
"""

from abc import ABC, abstractmethod


# ----------------------------------------------------
# 1. Abstraction: define a common interface for all items
# ----------------------------------------------------

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__is_checked_out = False   # encapsulated (private)

    @abstractmethod
    def item_type(self):
        pass

    def check_out(self):
        if self.__is_checked_out:
            print(f"'{self.title}' is already checked out!")
        else:
            self.__is_checked_out = True
            print(f"'{self.title}' checked out successfully.")

    def return_item(self):
        if not self.__is_checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self.__is_checked_out = False
            print(f"'{self.title}' returned successfully.")

    def is_available(self):
        return not self.__is_checked_out

    def info(self):
        status = "Available" if self.is_available() else "Checked Out"
        print(f"[{self.item_id}] {self.title} ({self.item_type()}) - {status}")


# ----------------------------------------------------
# 2. Inheritance: specific item types
# ----------------------------------------------------

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def item_type(self):
        return "Book"


class DVD(LibraryItem):
    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def item_type(self):
        return "DVD"


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def item_type(self):
        return "Magazine"


# ----------------------------------------------------
# 3. The Library class -> manages a collection of items
# ----------------------------------------------------

class Library:
    def __init__(self, name):
        self.name = name
        self.items = []          # list of LibraryItem objects (list from Day 21!)

    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item.title}' to {self.name}.")

    def show_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        for item in self.items:
            item.info()          # polymorphism: each item prints itself differently

    def find_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def available_items(self):
        # list comprehension (Day 25!)
        return [item for item in self.items if item.is_available()]


# ----------------------------------------------------
# 4. Putting it all together
# ----------------------------------------------------

library = Library("City Library")

library.add_item(Book("The Alchemist", "B001", "Paulo Coelho"))
library.add_item(DVD("Inception", "D001", 148))
library.add_item(Magazine("National Geographic", "M001", 254))
library.add_item(Book("Atomic Habits", "B002", "James Clear"))

library.show_catalog()

print("\n--- Checking out items ---")
book = library.find_item("B001")
book.check_out()

dvd = library.find_item("D001")
dvd.check_out()
dvd.check_out()   # trying to check out again -> already checked out

library.show_catalog()

print("\n--- Returning an item ---")
book.return_item()

print("\n--- Available items ---")
for item in library.available_items():
    item.info()

print("\n--- Trying to create an abstract LibraryItem directly ---")
try:
    generic = LibraryItem("Unknown", "X000")
except TypeError as e:
    print("Error:", e)


"""
📝 Quick Recap — Skills used in this project:
- Abstraction  : LibraryItem is an abstract base class (ABC)
- Inheritance  : Book, DVD, Magazine inherit from LibraryItem
- Encapsulation: __is_checked_out is private, controlled via methods
- Polymorphism : item_type() and info() behave differently per subclass
- Lists & list comprehension : Library stores/filters items
- This mirrors how real systems (e-commerce, inventory, school
  management apps) are structured using OOP principles.
"""