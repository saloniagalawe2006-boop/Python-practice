"""
🐍 Day 66: File Paths — pathlib Module
"""

from pathlib import Path

# ----------------------------------------------------
# 1. Why pathlib instead of plain strings?
# ----------------------------------------------------
# The old way used string concatenation for paths (error-prone,
# OS-dependent slashes). pathlib gives you a clean, OBJECT-oriented,
# cross-platform way to work with files and folders.


# ----------------------------------------------------
# 2. Creating a Path object
# ----------------------------------------------------

p = Path("sample_folder/data/file.txt")
print("Path:", p)
print("Type:", type(p))


# ----------------------------------------------------
# 3. Useful Path properties
# ----------------------------------------------------

print("\n--- Path properties ---")
print("Name (filename):", p.name)
print("Stem (name without extension):", p.stem)
print("Suffix (extension):", p.suffix)
print("Parent folder:", p.parent)
print("Parts:", p.parts)


# ----------------------------------------------------
# 4. Joining paths (the clean way, no manual '/' or '\')
# ----------------------------------------------------

base = Path("project")
full_path = base / "src" / "main.py"     # '/' operator joins paths!
print("\n--- Joining paths ---")
print("Joined path:", full_path)


# ----------------------------------------------------
# 5. Getting the current working directory
# ----------------------------------------------------

current_dir = Path.cwd()
print("\nCurrent working directory:", current_dir)


# ----------------------------------------------------
# 6. Creating folders and files
# ----------------------------------------------------

demo_dir = Path("demo_project")
demo_dir.mkdir(exist_ok=True)       # exist_ok=True avoids error if it already exists
print("\nCreated folder:", demo_dir)

sub_dir = demo_dir / "sub_folder"
sub_dir.mkdir(exist_ok=True)
print("Created nested folder:", sub_dir)

demo_file = demo_dir / "notes.txt"
demo_file.write_text("Hello from Day 66!")
print("Created file:", demo_file)


# ----------------------------------------------------
# 7. Checking existence and type
# ----------------------------------------------------

print("\n--- Checking paths ---")
print("Folder exists?", demo_dir.exists())
print("Is a directory?", demo_dir.is_dir())
print("File exists?", demo_file.exists())
print("Is a file?", demo_file.is_file())


# ----------------------------------------------------
# 8. Reading and writing files with pathlib
# ----------------------------------------------------

content = demo_file.read_text()
print("\nFile content:", content)

demo_file.write_text("Updated content on Day 66!")
print("Updated content:", demo_file.read_text())


# ----------------------------------------------------
# 9. Listing files in a directory
# ----------------------------------------------------

(demo_dir / "file1.txt").write_text("File 1")
(demo_dir / "file2.py").write_text("print('hello')")

print("\n--- Listing all items in demo_project ---")
for item in demo_dir.iterdir():
    print(item)


# ----------------------------------------------------
# 10. Finding files by pattern (glob)
# ----------------------------------------------------

print("\n--- Finding .txt files ---")
for txt_file in demo_dir.glob("*.txt"):
    print(txt_file)

print("\n--- Finding ALL files recursively (**) ---")
for any_file in demo_dir.rglob("*"):
    print(any_file)


# ----------------------------------------------------
# 11. Getting file size and other info
# ----------------------------------------------------

print("\n--- File info ---")
print("File size (bytes):", demo_file.stat().st_size)


# ----------------------------------------------------
# 12. Cleanup — remove all demo files/folders
# ----------------------------------------------------

for file in demo_dir.rglob("*"):
    if file.is_file():
        file.unlink()          # delete file

sub_dir.rmdir()                # remove empty subfolder
demo_dir.rmdir()                # remove empty main folder
print("\nDemo folder cleaned up.")


"""
📝 Quick Recap:
- from pathlib import Path
- Path("folder/file.txt")     -> creates a Path object
- .name, .stem, .suffix, .parent -> useful path components
- path1 / path2                -> joins paths (cross-platform!)
- Path.cwd()                   -> current working directory
- .mkdir(exist_ok=True)        -> create a folder
- .write_text() / .read_text() -> quick file write/read
- .exists() / .is_file() / .is_dir() -> check what a path is
- .iterdir()                   -> list items in a folder
- .glob(pattern) / .rglob(pattern) -> find files matching a pattern
- pathlib is the modern, recommended way to handle file paths
"""