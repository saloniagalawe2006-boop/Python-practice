"""
🐍 Day 57: The datetime Module (Deep Dive)
"""

from datetime import datetime, date, time, timedelta

# ----------------------------------------------------
# 1. Getting the current date and time
# ----------------------------------------------------

now = datetime.now()
today = date.today()

print("Current datetime:", now)
print("Current date:", today)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)


# ----------------------------------------------------
# 2. Creating a specific date/time manually
# ----------------------------------------------------

birthday = date(2003, 8, 15)
meeting = datetime(2026, 8, 6, 14, 30, 0)

print("\nBirthday:", birthday)
print("Meeting:", meeting)


# ----------------------------------------------------
# 3. Formatting dates as strings -> strftime()
# ----------------------------------------------------
# %Y = 4-digit year   %m = month   %d = day
# %H = hour (24h)     %M = minute  %S = second
# %B = full month name   %A = full weekday name

print("\n--- Formatting with strftime() ---")
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %B %d, %Y"))
print(now.strftime("%I:%M %p"))   # 12-hour format with AM/PM


# ----------------------------------------------------
# 4. Parsing a string INTO a datetime -> strptime()
# ----------------------------------------------------

date_string = "15-08-2003"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y")
print("\nParsed date:", parsed_date)
print("Parsed year:", parsed_date.year)


# ----------------------------------------------------
# 5. Date arithmetic using timedelta
# ----------------------------------------------------

print("\n--- Date arithmetic ---")
next_week = today + timedelta(weeks=1)
ten_days_ago = today - timedelta(days=10)
in_100_days = today + timedelta(days=100)

print("Today:", today)
print("Next week:", next_week)
print("10 days ago:", ten_days_ago)
print("100 days from now:", in_100_days)


# ----------------------------------------------------
# 6. Finding the difference between two dates
# ----------------------------------------------------

start_date = date(2026, 1, 1)
end_date = date(2026, 8, 6)
difference = end_date - start_date

print("\n--- Difference between dates ---")
print("Days between:", difference.days)


# ----------------------------------------------------
# 7. Calculating age from a birth date
# ----------------------------------------------------

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # subtract 1 if birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

print("\n--- Age calculation ---")
person_birthday = date(2003, 8, 15)
print(f"Age: {calculate_age(person_birthday)} years")


# ----------------------------------------------------
# 8. Comparing dates
# ----------------------------------------------------

date1 = date(2026, 8, 6)
date2 = date(2026, 12, 25)

print("\n--- Comparing dates ---")
print("date1 < date2:", date1 < date2)
print("date1 == date2:", date1 == date2)


# ----------------------------------------------------
# 9. Getting the day of the week
# ----------------------------------------------------

print("\n--- Day of the week ---")
print("weekday() (Mon=0):", today.weekday())
print("isoweekday() (Mon=1):", today.isoweekday())
print("Day name:", today.strftime("%A"))


# ----------------------------------------------------
# 10. Real-world example: countdown to a future event
# ----------------------------------------------------

event_date = date(2026, 12, 31)
days_remaining = (event_date - date.today()).days

print(f"\n--- Countdown ---")
print(f"Days until {event_date}: {days_remaining} days")


"""
📝 Quick Recap:
- datetime.now() / date.today()  -> current date & time
- date(y, m, d) / datetime(y, m, d, h, min, s) -> create specific dates
- strftime(format)  -> convert datetime OBJECT -> formatted STRING
- strptime(str, fmt) -> convert STRING -> datetime OBJECT
- timedelta(days=, weeks=, hours=...) -> add/subtract time spans
- date2 - date1  -> gives a timedelta with .days
- .weekday() / .isoweekday() -> get day of week as a number
- Common format codes: %Y %m %d %H %M %S %A %B %I %p
"""