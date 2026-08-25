"""
🐍 Day 69: Environment Variables & Config Files
os.environ, configparser
"""

import os
import configparser

# ----------------------------------------------------
# 1. What are environment variables?
# ----------------------------------------------------
# Values stored OUTSIDE your code (in the operating system),
# often used for secrets, API keys, and settings that change
# between environments (development, testing, production)
# — so you never hardcode sensitive data into your scripts.


# ----------------------------------------------------
# 2. Reading environment variables
# ----------------------------------------------------

# os.environ.get() is the SAFE way -> returns None if missing
path_var = os.environ.get("PATH")
print("PATH exists?", path_var is not None)

# Getting a variable that likely doesn't exist, with a default
api_key = os.environ.get("MY_APP_API_KEY", "default-key-not-set")
print("API key:", api_key)


# ----------------------------------------------------
# 3. Setting environment variables (for the current process only)
# ----------------------------------------------------

os.environ["MY_APP_API_KEY"] = "secret-12345"
os.environ["DEBUG_MODE"] = "True"

print("\n--- After setting ---")
print("API key:", os.environ.get("MY_APP_API_KEY"))
print("Debug mode:", os.environ.get("DEBUG_MODE"))

# NOTE: env variables are always strings! Convert types manually.
debug_mode = os.environ.get("DEBUG_MODE") == "True"
print("Debug mode (as bool):", debug_mode, type(debug_mode))


# ----------------------------------------------------
# 4. Real-world pattern: using env vars for configuration
# ----------------------------------------------------

def get_database_url():
    return os.environ.get("DATABASE_URL", "sqlite:///default.db")

print("\nDatabase URL:", get_database_url())


# ----------------------------------------------------
# 5. Using a .env file (common in real projects)
# ----------------------------------------------------
# In real projects, secrets go in a .env file (NEVER committed
# to git) and are loaded using the 'python-dotenv' package:
#
#   pip install python-dotenv
#
#   from dotenv import load_dotenv
#   load_dotenv()   # loads variables from a .env file into os.environ
#
# .env file content example:
#   API_KEY=abc123
#   DEBUG=True


# ----------------------------------------------------
# 6. Config files with configparser (.ini style)
# ----------------------------------------------------
# Useful for structured app settings that AREN'T secrets.

config = configparser.ConfigParser()

config["DATABASE"] = {
    "host": "localhost",
    "port": "5432",
    "name": "myapp_db"
}

config["APP"] = {
    "debug": "True",
    "max_connections": "100"
}

with open("settings.ini", "w") as configfile:
    config.write(configfile)

print("\nConfig file written: settings.ini")


# ----------------------------------------------------
# 7. Reading a config file
# ----------------------------------------------------

reader = configparser.ConfigParser()
reader.read("settings.ini")

print("\n--- Reading settings.ini ---")
print("Sections:", reader.sections())
print("Database host:", reader["DATABASE"]["host"])
print("Database port:", reader["DATABASE"]["port"])
print("App debug (string):", reader["APP"]["debug"])

# configparser has helper methods for type conversion
print("App debug (as bool):", reader.getboolean("APP", "debug"))
print("Max connections (as int):", reader.getint("APP", "max_connections"))


# ----------------------------------------------------
# 8. Updating a config value
# ----------------------------------------------------

reader["APP"]["max_connections"] = "200"
with open("settings.ini", "w") as configfile:
    reader.write(configfile)

reader.read("settings.ini")
print("\nUpdated max_connections:", reader["APP"]["max_connections"])


# ----------------------------------------------------
# 9. Looping through all config sections and keys
# ----------------------------------------------------

print("\n--- All settings ---")
for section in reader.sections():
    print(f"[{section}]")
    for key, value in reader[section].items():
        print(f"  {key} = {value}")


# ----------------------------------------------------
# 10. Cleanup
# ----------------------------------------------------

os.remove("settings.ini")
print("\nDemo config file cleaned up.")


"""
📝 Quick Recap:
- os.environ.get(key, default)  -> safely read an env variable
- os.environ[key] = value       -> set an env var (current process only)
- Env vars are ALWAYS strings -> manually convert to bool/int as needed
- .env files + python-dotenv    -> common way to load local secrets
- configparser -> reads/writes structured .ini config files
- config["SECTION"]["key"]       -> access nested settings
- reader.getboolean() / getint() -> type-safe config value reading
- Rule of thumb: SECRETS -> environment variables,
  general SETTINGS -> config files (.ini/.json/.yaml)
"""