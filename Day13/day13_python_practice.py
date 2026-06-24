# ============================================================
# Day 13 - Default & Keyword Arguments (Full Depth)
# File: day13_default_keyword_args.py
# ============================================================


# ── SECTION 1: Basic Default Parameter ───────────────────────

def order_coffee(size="Medium", sugar="Regular"):
    print(f"Order: {size} coffee with {sugar} sugar.")

order_coffee()
# No arguments given at all -> BOTH defaults are used

order_coffee("Large")
# Only 'size' is given -> 'sugar' still uses its default "Regular"

order_coffee("Small", "Extra")
# Both given -> both defaults are overridden


# ── SECTION 2: Rule — Non-Default Parameters Must Come FIRST ──

def book_ticket(destination, seat_type="Economy", meal="Veg"):
    print(f"Ticket to {destination}: {seat_type} seat, {meal} meal.")

book_ticket("Goa")
book_ticket("Delhi", "Business")
book_ticket("Mumbai", meal="Non-Veg")
# 'destination' has NO default -> it is REQUIRED, must always be provided
# 'seat_type' and 'meal' have defaults -> they are OPTIONAL

# ❌ This would CRASH if uncommented - cannot have default BEFORE non-default:
# def invalid_order(seat_type="Economy", destination):
#     pass


# ── SECTION 3: Keyword Arguments — Naming Values Explicitly ───

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

create_profile(name="Rahul", city="Mumbai", age=22)
# Order is COMPLETELY different from the function definition,
# but it works perfectly because every value is explicitly named.

create_profile("Priya", city="Delhi", age=25)
# Mixing: "Priya" is positional (goes to 'name' by position)
# city= and age= are keyword (named directly)


# ── SECTION 4: The Strict Ordering Rule ───────────────────────

def describe_trip(destination, days, budget="Medium", guide=True):
    print(f"Trip to {destination} for {days} days. Budget: {budget}. Guide: {guide}")

describe_trip("Kerala", 5)
describe_trip("Goa", 3, "Low")
describe_trip("Manali", 7, budget="High", guide=False)
describe_trip("Jaipur", days=4, budget="Low")
# RULE ORDER when calling: positional arguments FIRST, then keyword arguments.
# RULE ORDER when defining: non-default parameters FIRST, then default ones.


# ── SECTION 5: The Mutable Default Trap (IMPORTANT Python Gotcha) ─

def add_item_wrong(item, cart=[]):
    cart.append(item)
    return cart

print("\n--- The Mutable Default Trap ---")
print(add_item_wrong("apple"))
print(add_item_wrong("banana"))
# ⚠️ You'd EXPECT each call to start with a fresh empty list, but:
# Python creates the default list [] only ONCE, when the function is DEFINED.
# Every call that doesn't provide its own 'cart' REUSES the SAME list!

def add_item_correct(item, cart=None):
    if cart is None:
        cart = []          # a fresh empty list created INSIDE the function, every call
    cart.append(item)
    return cart

print("\n--- The Correct Fix ---")
print(add_item_correct("apple"))
print(add_item_correct("banana"))
# Now each call correctly starts fresh, because 'cart' is created freshly each time.


# ── SECTION 6: *args — Accepting Any Number of Positional Arguments ─

def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
    # *numbers collects ANY number of arguments into a tuple automatically

print("\n--- *args preview ---")
print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))
print(add_all())


# ── SECTION 7: **kwargs — Accepting Any Number of Keyword Arguments ─

def print_profile(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")
    # **details collects ANY number of keyword arguments into a dictionary automatically
    # (dictionaries covered fully on Day 25)

print("\n--- **kwargs preview ---")
print_profile(name="Vikram", age=28, city="Pune")
print_profile(name="Sneha", profession="Engineer")


# ── SECTION 8: Combining Everything Together ──────────────────

def create_order(item, quantity=1, *extra_items, **special_instructions):
    print(f"Main item: {item} x{quantity}")
    if extra_items:
        print(f"Extra items: {extra_items}")
    if special_instructions:
        print(f"Special instructions: {special_instructions}")

print("\n--- Combining all argument types ---")
create_order("Pizza")
create_order("Pizza", 2)
create_order("Pizza", 2, "Garlic Bread", "Coke")
create_order("Pizza", 2, "Garlic Bread", spice_level="High", extra_cheese=True)


# ── SECTION 9: Practical — Flexible Greeting Function ──────────

def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print("\n--- Flexible Greeting ---")
print(greet("Rahul"))
print(greet("Priya", "Welcome"))
print(greet("Anjali", greeting="Good morning", punctuation="."))
print(greet(name="Vikram", punctuation="?", greeting="Hey"))


# ── SECTION 10: Practical — Discount Calculator with Defaults ──

def calculate_price(original_price, discount_percent=10, is_member=False):
    discount_amount = original_price * (discount_percent / 100)
    if is_member:
        discount_amount += original_price * 0.05    # extra 5% for members
    final_price = original_price - discount_amount
    return round(final_price, 2)

print("\n--- Discount Calculator ---")
print(f"Default discount: Rs. {calculate_price(1000)}")
print(f"20% discount: Rs. {calculate_price(1000, 20)}")
print(f"20% + member: Rs. {calculate_price(1000, 20, True)}")
print(f"Member only (default discount): Rs. {calculate_price(1000, is_member=True)}")

# ============================================================
# END OF DAY 13
# ============================================================