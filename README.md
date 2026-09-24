# Student Record Management System

A console-based mini project built in Python that lets you add, view, search, update, and delete student records — with all data saved permanently to a JSON file.

Built as an MCA mini project to demonstrate core Python concepts in a single, working application: data types, conditionals, loops, functions, exception handling, file I/O, and menu-driven program design.

## Features

- **Add** a new student record (with validation and duplicate-ID checking)
- **View** all stored records
- **Search** for a record by Student ID
- **Update** a single field of an existing record
- **Delete** a record (with confirmation prompt)
- **Persistent storage** — records are saved to `students.json` and reloaded automatically the next time the program runs
- Graceful handling of invalid input, missing files, and corrupted data — the program never crashes on bad input

## Tech Stack

- Python 3 (standard library only — no external dependencies)
- JSON for data storage

## Project Structure

```
student-record-management/
├── student_records.py   # main program
├── students.json         # auto-created on first save (do not create manually)
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.6 or later

### Installation

```bash
git clone https://github.com/<your-username>/student-record-management.git
cd student-record-management
```

No dependencies to install — the project only uses Python's built-in `json` module.

### Usage

Run the program from the project folder:

```bash
python3 student_records.py
```

You'll see a menu like this:

```
===== Student Record Management System =====
1. Add Record
2. View Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
==============================================
Enter your choice:
```

Enter a number to choose an action. Your records are automatically saved to `students.json` after every add, update, or delete — so closing and reopening the program won't lose your data.

## Each Student Record

| Field | Type | Example |
|---|---|---|
| Student ID | string | `"101"` |
| Name | string | `"Riya Sharma"` |
| Age | integer | `21` |
| Course | string | `"MCA"` |
| Email | string | `"riya@example.com"` |
| Phone | string | `"9876543210"` |

## Concepts Demonstrated

| Concept | Where |
|---|---|
| Data Types & Variables | `str` for id/name/course/email/phone, `int` for age |
| Conditional Statements | `if/elif/else` for menu routing and validation |
| Loops | `while True` for the menu; `for` loops in `view_records()` and `find_student_by_id()` |
| Functions | One function per responsibility (see below) |
| Exception Handling | `try/except` for invalid input, missing/corrupt files |
| File I/O | `load_records()` / `save_records()` using the `json` module |
| Menu-driven Design | `display_menu()` + the main loop in `main()` |

## Functions

| Function | Purpose |
|---|---|
| `load_records()` | Loads records from `students.json` at startup |
| `save_records(records)` | Writes the current records back to the file |
| `find_student_by_id(records, id)` | Shared helper used by search, update, and delete |
| `display_menu()` | Prints the menu |
| `add_record(records)` | Adds a new, validated record |
| `view_records(records)` | Displays all records |
| `search_record(records)` | Finds and displays a record by ID |
| `update_record(records)` | Updates one field of an existing record |
| `delete_record(records)` | Deletes a record after confirmation |
| `main()` | Runs the menu loop and ties everything together |

## Testing

| Test Case | Input | Expected Result |
|---|---|---|
| Add valid record | Valid details | Record added and saved |
| Duplicate ID | Existing ID | Error, record not added |
| Invalid age | `"abc"` | Error, record not added |
| Search existing ID | Existing ID | Record displayed |
| Search invalid ID | Non-existing ID | "Not found" message |
| Update record | Existing ID + new value | Field updated and saved |
| Delete record | Existing ID + `y` | Record removed and saved |
| Missing file | No `students.json` | Starts with empty list, no crash |
| Exit | `6` | Program closes cleanly |

## Notes

- This project intentionally avoids advanced concepts (classes, decorators, databases) to keep the code beginner-friendly and fully explainable.
- Built as Assignment 1 for the MCA curriculum.

## License

This project is open for educational use.
