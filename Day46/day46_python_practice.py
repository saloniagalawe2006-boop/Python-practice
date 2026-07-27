"""
🐍 Day 46: Regular Expressions (regex)
"""

import re

# ----------------------------------------------------
# 1. What is Regex?
# ----------------------------------------------------
# Regular expressions are patterns used to SEARCH, MATCH,
# and MANIPULATE text based on rules, not exact strings.
# Python's 're' module handles all regex operations.


# ----------------------------------------------------
# 2. re.search() -> find the FIRST match anywhere in the string
# ----------------------------------------------------

text = "My phone number is 9876543210."

match = re.search(r"\d+", text)   # \d+ means "one or more digits"
if match:
    print("Found number:", match.group())


# ----------------------------------------------------
# 3. re.match() -> checks only at the START of the string
# ----------------------------------------------------

result1 = re.match(r"My", text)
result2 = re.match(r"phone", text)

print("\nMatch 'My' at start:", bool(result1))
print("Match 'phone' at start:", bool(result2))   # False - not at the start


# ----------------------------------------------------
# 4. re.findall() -> find ALL matches in the string
# ----------------------------------------------------

sentence = "Call 9876543210 or 9123456789 for support."
all_numbers = re.findall(r"\d+", sentence)
print("\nAll numbers found:", all_numbers)


# ----------------------------------------------------
# 5. re.sub() -> replace matches with something else
# ----------------------------------------------------

masked = re.sub(r"\d", "*", sentence)
print("\nMasked numbers:", masked)


# ----------------------------------------------------
# 6. Common regex patterns (cheat sheet)
# ----------------------------------------------------
# \d  -> digit           \D -> non-digit
# \w  -> word character  \W -> non-word character
# \s  -> whitespace      \S -> non-whitespace
# .   -> any character (except newline)
# +   -> one or more     *  -> zero or more
# ?   -> zero or one     {n} -> exactly n times
# ^   -> start of string $  -> end of string

print("\n--- Cheat sheet in action ---")
print("Words only:", re.findall(r"\w+", "Hello, World! 123"))
print("Digits only:", re.findall(r"\d+", "Hello, World! 123"))


# ----------------------------------------------------
# 7. Validating an email address
# ----------------------------------------------------

def is_valid_email(email):
    pattern = r"^[\w.]+@[\w]+\.[a-z]{2,}$"
    return bool(re.match(pattern, email))

print("\n--- Email validation ---")
print("rahul@gmail.com  ->", is_valid_email("rahul@gmail.com"))
print("invalid-email    ->", is_valid_email("invalid-email"))
print("priya.k@abc.co   ->", is_valid_email("priya.k@abc.co"))


# ----------------------------------------------------
# 8. Validating a phone number (10 digits)
# ----------------------------------------------------

def is_valid_phone(number):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern, number))

print("\n--- Phone validation ---")
print("9876543210 ->", is_valid_phone("9876543210"))
print("98765      ->", is_valid_phone("98765"))
print("98765abcde ->", is_valid_phone("98765abcde"))


# ----------------------------------------------------
# 9. Splitting text using regex
# ----------------------------------------------------

messy_text = "apple, banana;  cherry , mango"
items = re.split(r"[,;]\s*", messy_text)
print("\nSplit result:", items)


# ----------------------------------------------------
# 10. Real-world example: extracting all emails from text
# ----------------------------------------------------

document = "Contact us at support@shop.com or sales@shop.com for help."
emails = re.findall(r"[\w.]+@[\w.]+", document)
print("\nExtracted emails:", emails)


"""
📝 Quick Recap:
- import re
- re.search(pattern, text)  -> finds first match ANYWHERE
- re.match(pattern, text)   -> checks match at the START only
- re.findall(pattern, text) -> returns ALL matches as a list
- re.sub(pattern, repl, text) -> replaces matches with something else
- re.split(pattern, text)  -> splits text using a pattern as separator
- Use raw strings r"..." for patterns to avoid backslash escaping issues
- Great for: validating emails/phone numbers, extracting data,
  cleaning messy text, parsing logs
"""