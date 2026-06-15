# ============================================================
# Day 04 - String Methods
# File: day04_string_methods.py
# ============================================================


# ── SECTION 1: Case Methods ───────────────────────────────────

name = "rahul sharma"

print(name.upper())       # RAHUL SHARMA
print(name.lower())       # rahul sharma
print(name.title())       # Rahul Sharma
print(name.capitalize())  # Rahul sharma
print(name.swapcase())    # RAHUL SHARMA

print(name)
# Still prints: rahul sharma
# Methods do NOT change the original. They return a NEW string.

saved = name.upper()
print(saved)              # RAHUL SHARMA


# ── SECTION 2: Whitespace Methods ────────────────────────────

messy = "   Hello Python!   "

print(messy.strip())      # "Hello Python!"
print(messy.lstrip())     # "Hello Python!   "
print(messy.rstrip())     # "   Hello Python!"


# ── SECTION 3: Find Methods ───────────────────────────────────

sentence = "Python is fun and Python is powerful"

print(sentence.find("Python"))      # 0
print(sentence.find("Java"))        # -1
print(sentence.count("Python"))     # 2
print(sentence.startswith("Py"))    # True
print(sentence.endswith("ful"))     # True

print("fun" in sentence)            # True
print("Java" in sentence)           # False


# ── SECTION 4: Replace Method ─────────────────────────────────

text = "I love Java. Java is great."

print(text.replace("Java", "Python"))      # replaces ALL
print(text.replace("Java", "Python", 1))   # replaces only FIRST


# ── SECTION 5: Split and Join ────────────────────────────────

data = "Rahul,Priya,Anjali,Vikram"

names = data.split(",")
print(names)                        # ['Rahul', 'Priya', 'Anjali', 'Vikram']

words = "Hello World Python".split()
print(words)                        # ['Hello', 'World', 'Python']

joined = " - ".join(names)
print(joined)                       # Rahul - Priya - Anjali - Vikram


# ── SECTION 6: Length with len() ─────────────────────────────

word = "Programming"
print(len(word))                    # 11

sentence2 = "Hello World"
print(len(sentence2))               # 11  (space counts!)


# ── SECTION 7: Indexing ───────────────────────────────────────

language = "Python"
#            012345

print(language[0])     # P
print(language[1])     # y
print(language[5])     # n
print(language[-1])    # n
print(language[-2])    # o


# ── SECTION 8: Slicing ────────────────────────────────────────

text2 = "Hello, Python!"
#        01234567890123

print(text2[0:5])      # Hello
print(text2[7:13])     # Python
print(text2[:5])       # Hello
print(text2[7:])       # Python!
print(text2[-7:-1])    # Python
print(text2[::2])      # Hl,Pto
print(text2[::-1])     # !nohtyP ,olleH


# ── SECTION 9: Checking Methods ──────────────────────────────

print("hello".isalpha())      # True
print("hello123".isalpha())   # False
print("123".isdigit())        # True
print("12.5".isdigit())       # False
print("Hello123".isalnum())   # True
print("   ".isspace())        # True


# ── SECTION 10: Real World — Input Cleaner ────────────────────

print("\n--- Name Cleaner ---")
raw = input("Type your name (messy is fine): ")

cleaned   = raw.strip()
formatted = cleaned.title()

print(f"Original  : '{raw}'")
print(f"Cleaned   : '{cleaned}'")
print(f"Formatted : '{formatted}'")
print(f"Uppercase : '{formatted.upper()}'")
print(f"Length    : {len(formatted)} characters")
print(f"Starts with A: {formatted.startswith('A')}")


# ============================================================
# END OF DAY 04
# ============================================================