# ============================================================
# Day 17 - String Slicing (Advanced Deep Dive)
# File: day17_string_slicing.py
# ============================================================


# ── SECTION 1: Recap — Basic Slicing ─────────────────────────

text = "PYTHON PROGRAMMING"
#       0123456789...

print(text[0:6])        # PYTHON
print(text[7:])         # PROGRAMMING
print(text[:6])         # PYTHON
print(text[:])          # PYTHON PROGRAMMING (entire string - a FULL COPY)


# ── SECTION 2: Negative Indices in Slicing ────────────────────

print(text[-11:])        # PROGRAMMING (last 11 characters)
print(text[:-12])        # PYTHON (everything except the last 12 characters)
print(text[-11:-1])      # PROGRAMMIN (from -11 up to, but NOT including, -1)


# ── SECTION 3: The step Parameter in Depth ────────────────────

numbers_str = "0123456789"

print(numbers_str[::2])     # 02468  - every 2nd character, starting from index 0
print(numbers_str[1::2])    # 13579  - every 2nd character, starting from index 1
print(numbers_str[::3])     # 0369   - every 3rd character
print(numbers_str[::-1])    # 9876543210 - REVERSED (negative step goes backward)
print(numbers_str[::-2])    # 97531 - reversed, every 2nd character


# ── SECTION 4: Combining start, stop, AND a Negative Step ──────

print(numbers_str[8:2:-1])
# Going BACKWARD from index 8 down to (but not including) index 2
# Output: 876543

print(numbers_str[::-1][2:5])
# First reverse the whole string, THEN slice the reversed result
# Reversed: "9876543210" -> slice [2:5] -> "765"


# ── SECTION 5: Slicing Beyond the String's Length (No Crash!) ──

short_word = "Hi"

print(short_word[0:100])    # Hi  - Python just stops at the actual end, no error
print(short_word[50:60])    # ''  - empty string, completely out of range but NO crash
print(short_word[-100:])    # Hi  - negative index way beyond start, Python clips it safely

# Compare this to regular indexing, which DOES crash if out of range:
# print(short_word[10])      # ❌ This WOULD crash: IndexError: string index out of range
# Slicing is much more forgiving than direct indexing!


# ── SECTION 6: Strings are Immutable — Slicing Creates COPIES ──

original = "Hello"
sliced = original[1:4]

print(f"Original: {original}")
print(f"Sliced  : {sliced}")

# original[0] = "J"    # ❌ This would CRASH: 'str' object does not support item assignment
# Strings CANNOT be changed in place. Slicing always creates a brand NEW string.

modified = "J" + original[1:]
print(f"Modified (new string): {modified}")
# This is how you "change" a string in Python - build a NEW one using slices + concatenation


# ── SECTION 7: Practical — Reversing Words in a Sentence ───────

sentence = "Python is an amazing language"

words = sentence.split()           # split into a list of words (Day 4 recap)
reversed_words = words[::-1]       # reverse the ORDER of words using slicing
result = " ".join(reversed_words)  # join them back into a sentence

print(f"\nOriginal: {sentence}")
print(f"Reversed words: {result}")

# Reversing each individual letter, but keeping word order:
letters_reversed = " ".join(word[::-1] for word in words)
print(f"Letters reversed: {letters_reversed}")


# ── SECTION 8: Practical — Palindrome Checker ──────────────────

def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
    # Compare the cleaned string to its own reverse - if equal, it's a palindrome!

print("\n--- Palindrome Checker ---")
test_words = ["madam", "hello", "racecar", "Nurses Run", "python"]

for word in test_words:
    result = "YES" if is_palindrome(word) else "NO"
    print(f"  '{word}': {result}")


# ── SECTION 9: Practical — Extracting Parts of Structured Text ─

phone_number = "9876543210"

country_style = f"+91-{phone_number[:5]}-{phone_number[5:]}"
print(f"\nFormatted phone: {country_style}")

date_string = "28-06-2026"
day_part   = date_string[0:2]
month_part = date_string[3:5]
year_part  = date_string[6:]

print(f"Day: {day_part}, Month: {month_part}, Year: {year_part}")


# ── SECTION 10: Practical — Masking Sensitive Data ─────────────

card_number = "1234567812345678"

masked = card_number[:4] + "*" * 8 + card_number[-4:]
print(f"\nOriginal card: {card_number}")
print(f"Masked card  : {masked}")

email = "rahul.sharma@gmail.com"
username, domain = email.split("@")
masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
masked_email = masked_username + "@" + domain
print(f"Original email: {email}")
print(f"Masked email  : {masked_email}")


# ── SECTION 11: Practical — Chunking a String into Equal Parts ──

code = "ABCDEFGHIJ"
chunk_size = 3

print(f"\nOriginal code: {code}")
print("Chunks of 3:")
for i in range(0, len(code), chunk_size):
    print(f"  {code[i:i+chunk_size]}")
# range(0, len(code), chunk_size) jumps in steps of 3,
# and code[i:i+chunk_size] grabs each chunk using that starting point

# ============================================================
# END OF DAY 17
# ============================================================