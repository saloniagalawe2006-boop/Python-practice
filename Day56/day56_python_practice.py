"""
🐍 Day 56: The logging Module
"""

import logging

# ----------------------------------------------------
# 1. Why logging instead of print()?
# ----------------------------------------------------
# print() is fine for quick debugging, but logging gives you:
#   - Severity LEVELS (info, warning, error...)
#   - Timestamps automatically
#   - Easy on/off control without deleting code
#   - Ability to save logs to a FILE for later review
#   - Used in every real production application


# ----------------------------------------------------
# 2. The 5 logging levels (lowest to highest severity)
# ----------------------------------------------------
# DEBUG    -> detailed info, useful only while developing
# INFO     -> general confirmation things are working
# WARNING  -> something unexpected, but not breaking
# ERROR    -> a real problem occurred
# CRITICAL -> a serious error, program may not continue

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

print("--- Basic logging levels ---")
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")


# ----------------------------------------------------
# 3. By default, only WARNING and above show (unless configured)
# ----------------------------------------------------
# Note: basicConfig() only works the FIRST time it's called in a run.
# That's why we set level=DEBUG above to see everything.


# ----------------------------------------------------
# 4. Creating a custom logger (recommended for real projects)
# ----------------------------------------------------

logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)
logger.propagate = False   # stop messages from also going to the root logger (avoids duplicate lines)

# Console handler -> prints to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter -> controls what each log line looks like
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

print("\n--- Custom logger ---")
logger.debug("Debug won't show (handler level is INFO)")
logger.info("Application started successfully.")
logger.warning("Low disk space detected.")


# ----------------------------------------------------
# 5. Logging to a FILE
# ----------------------------------------------------

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("This debug message goes to the FILE (not console).")
logger.error("Something went wrong! Logged to file too.")

print("\nLogs also written to app.log")


# ----------------------------------------------------
# 6. Real-world example: logging inside a function
# ----------------------------------------------------

def divide(a, b):
    logger.info(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted!")
        return None

print("\n--- Logging inside a function ---")
divide(10, 2)
divide(10, 0)


# ----------------------------------------------------
# 7. Reading back the log file
# ----------------------------------------------------

print("\n--- Contents of app.log ---")
with open("app.log", "r") as f:
    print(f.read())


# ----------------------------------------------------
# 8. Cleanup demo file
# ----------------------------------------------------

import os
file_handler.close()
logger.removeHandler(file_handler)
os.remove("app.log")
print("Demo log file cleaned up.")


"""
📝 Quick Recap:
- import logging
- Levels (low -> high): DEBUG < INFO < WARNING < ERROR < CRITICAL
- logging.basicConfig(level=..., format=...) -> quick global setup
- logging.getLogger(name) -> create a custom, named logger
- Handlers control WHERE logs go: StreamHandler (console),
  FileHandler (file)
- Formatter controls HOW each log line looks (timestamp, level, etc.)
- Use logging instead of print() in real applications for
  better debugging, monitoring, and production-readiness
"""