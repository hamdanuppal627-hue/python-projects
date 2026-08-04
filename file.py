import csv
import json
import os

# Define file names used in this script
TXT_FILE = "demo_notes.txt"
CSV_FILE = "demo_grades.csv"
JSON_FILE = "demo_config.json"


def basic_text_operations():
    """Demonstrates writing, appending, and reading standard text files."""
    print("--- 1. Running Basic Text Operations ---")

    # Step A: Writing to a file (Creates new or overwrites)
    print(f"Writing initial text to {TXT_FILE}...")
    with open(TXT_FILE, "w", encoding="utf-8") as file:
        file.write("Python File Handling Demo\n")
        file.write("=========================\n")
        file.write("Line 1: Initial setup complete.\n")

    # Step B: Appending data (Adds to the end without erasing)
    print(f"Appending extra lines to {TXT_FILE}...")
    with open(TXT_FILE, "a", encoding="utf-8") as file:
        file.write("Line 2: New log entry appended.\n")
        file.write("Line 3: Another system message.\n")

    # Step C: Reading line-by-line efficiently
    print(f"Reading content from {TXT_FILE} line-by-line:")
    with open(TXT_FILE, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            # .strip() removes hidden trailing newlines (\n)
            print(f"  [Row {index}] -> {line.strip()}")
    print()


def structured_data_operations():
    """Demonstrates handling spreadsheets (CSV) and configurations (JSON)."""
    print("--- 2. Running Structured Data Operations ---")

    # Step A: CSV (Comma-Separated Values) handling
    student_data = [
        ["Name", "Subject", "Score"],
        ["Alice", "Math", "95"],
        ["Bob", "Physics", "88"],
        ["Charlie", "Chemistry", "92"]
    ]
    
    print(f"Saving tabular data to {CSV_FILE}...")
    # newline="" prevents extra blank lines on certain operating systems
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(student_data)

    print(f"Reading back data from {CSV_FILE}:")
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"  Parsed Row: {row}")

    # Step B: JSON (JavaScript Object Notation) handling
    settings_dict = {
        "app_name": "FileMaster",
        "version": 2.4,
        "features": ["auto_save", "dark_mode", "cloud_sync"]
    }

    print(f"\nSaving configuration dictionary to {JSON_FILE}...")
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        # indent=4 formats the JSON visually with indentation spaces
        json.dump(settings_dict, file, indent=4)

    print(f"Reading settings back from {JSON_FILE}:")
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        loaded_settings = json.load(file)
        print(f"  App Name: {loaded_settings['app_name']}")
        print(f"  Enabled Features: {', '.join(loaded_settings['features'])}")
    print()


def safe_error_handling(target_filename):
    """Demonstrates protecting code from crashing using try-except blocks."""
    print("--- 3. Running Safe Error Handling Demo ---")
    print(f"Attempting to open a potentially risky file: '{target_filename}'")
    
    try:
        with open(target_filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("  Success! File content loaded.")
            
    except FileNotFoundError:
        print(f"  [Caught Error]: The file '{target_filename}' does not exist on disk.")
        
    except PermissionError:
        print(f"  [Caught Error]: You lack administrative permissions to open '{target_filename}'.")
        
    except Exception as unexpected_err:
        print(f"  [Caught Error]: An unhandled issue occurred: {unexpected_err}")
    print()


def clean_up_files():
    """Removes the generated files to keep your workspace tidy."""
    print("--- 4. Cleaning Up Workspace ---")
    files_to_remove = [TXT_FILE, CSV_FILE, JSON_FILE]
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  Deleted temp file: {filename}")
        else:
            print(f"  File not found for deletion: {filename}")


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print("=== STARTING COMPLETE PYTHON FILE HANDLING SYSTEM ===\n")
    
    # 1. Run basic text handling (Write, Append, Read)
    basic_text_operations()
    
    # 2. Run structured formats (CSV and JSON)
    structured_data_operations()
    
    # 3. Test error handling with a file that deliberately does not exist
    safe_error_handling("missing_secret_file.conf")
    
    # 4. Optional: Clean up created files so your folder stays clean
    clean_up_files()
    
    print("\n=== PROGRAM COMPLETED SUCCESSFULLY ===")
