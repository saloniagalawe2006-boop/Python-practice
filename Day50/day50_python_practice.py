"""
🐍 Day 50: Milestone Mini Project — Contact Book Manager
Combines everything from Day 31-49:
Functions, Lambda, Recursion, Modules, Error Handling,
File Handling, OOP (Classes/Inheritance/Encapsulation/
Polymorphism/Abstraction), Iterators/Generators, Decorators,
Regex, JSON, CSV, Built-in Functions
"""

import re
import json
import csv
import os
from functools import reduce


# ----------------------------------------------------
# 1. Decorator: logs every action performed (Day 45)
# ----------------------------------------------------

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ----------------------------------------------------
# 2. Contact class -> uses encapsulation (Day 40)
# ----------------------------------------------------

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.__phone = phone     # private attribute
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if self.is_valid_phone(value):
            self.__phone = value
        else:
            print(f"Invalid phone number: {value}")

    @property
    def email(self):
        return self.__email

    @staticmethod
    def is_valid_phone(number):                       # regex (Day 46)
        return bool(re.match(r"^\d{10}$", number))

    @staticmethod
    def is_valid_email(email):                          # regex (Day 46)
        return bool(re.match(r"^[\w.]+@[\w]+\.[a-z]{2,}$", email))

    def to_dict(self):
        return {"name": self.name, "phone": self.__phone, "email": self.__email}

    def __str__(self):                                   # polymorphism (Day 41)
        return f"{self.name} | {self.__phone} | {self.__email}"


# ----------------------------------------------------
# 3. ContactBook class -> manages the collection
# ----------------------------------------------------

class ContactBook:
    def __init__(self):
        self.contacts = []      # list of Contact objects

    @log_action
    def add_contact(self, name, phone, email):
        if not Contact.is_valid_phone(phone):
            print(f"Skipped '{name}': invalid phone number.")
            return
        if not Contact.is_valid_email(email):
            print(f"Skipped '{name}': invalid email.")
            return
        self.contacts.append(Contact(name, phone, email))
        print(f"Added contact: {name}")

    @log_action
    def remove_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name != name]   # list comp (Day 25)
        if len(self.contacts) < original_count:
            print(f"Removed contact: {name}")
        else:
            print(f"No contact found with name: {name}")

    def find_contact(self, name):
        for contact in self.contacts:      # iteration (Day 44)
            if contact.name == name:
                return contact
        return None

    def show_all(self):
        print("\n--- All Contacts ---")
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(contact)

    def total_contacts(self):
        return len(self.contacts)

    @log_action
    def save_to_json(self, filename):
        data = [c.to_dict() for c in self.contacts]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)     # JSON (Day 47)
        print(f"Saved {len(data)} contacts to {filename}")

    @log_action
    def load_from_json(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.contacts = [Contact(d["name"], d["phone"], d["email"]) for d in data]
            print(f"Loaded {len(self.contacts)} contacts from {filename}")
        except FileNotFoundError:            # error handling (Day 36)
            print(f"File '{filename}' not found.")

    @log_action
    def export_to_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows([c.to_dict() for c in self.contacts])     # CSV (Day 48)
        print(f"Exported contacts to {filename}")


# ----------------------------------------------------
# 4. Using the ContactBook
# ----------------------------------------------------

book = ContactBook()

book.add_contact("Rahul", "9876543210", "rahul@gmail.com")
book.add_contact("Priya", "9123456789", "priya@gmail.com")
book.add_contact("Anjali", "9988776655", "anjali@gmail.com")
book.add_contact("BadContact", "12345", "not-an-email")   # invalid, will be skipped

book.show_all()
print("\nTotal contacts:", book.total_contacts())


# ----------------------------------------------------
# 5. Search and remove
# ----------------------------------------------------

print("\n--- Searching ---")
found = book.find_contact("Priya")
print("Found:", found if found else "Not found")

book.remove_contact("Priya")
book.show_all()


# ----------------------------------------------------
# 6. Save, reload, and export
# ----------------------------------------------------

book.save_to_json("contacts.json")

new_book = ContactBook()
new_book.load_from_json("contacts.json")
new_book.show_all()

new_book.export_to_csv("contacts.csv")

with open("contacts.csv", "r") as f:
    print("\n--- CSV file content ---")
    print(f.read())


# ----------------------------------------------------
# 7. Bonus: functional-style summary using built-ins (Day 49)
# ----------------------------------------------------

all_names = list(map(lambda c: c.name, new_book.contacts))
name_lengths = reduce(lambda a, b: a + b, map(len, all_names))

print("--- Summary ---")
print("All names:", all_names)
print("Total characters across all names:", name_lengths)


# ----------------------------------------------------
# 8. Cleanup demo files
# ----------------------------------------------------

os.remove("contacts.json")
os.remove("contacts.csv")
print("\nDemo files cleaned up.")


"""
📝 Quick Recap — Skills used in this milestone project:
- Functions, decorators (@log_action, @staticmethod, @property)
- OOP: Contact (encapsulation) + ContactBook (composition)
- Regex validation for phone/email
- JSON save/load, CSV export
- Error handling for missing files
- List comprehensions, map/reduce, iteration
- This mirrors a real small CRM/contact management tool!
"""