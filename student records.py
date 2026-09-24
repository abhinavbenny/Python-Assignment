import json

DATA_FILE = "students.json"

def load_records():
    """Load records from the JSON file. Return an empty list if the
    file doesn't exist or contains invalid/corrupted data."""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Warning: data file format looks wrong. Starting with an empty list.")
                return []
    except FileNotFoundError:
        # First time running the program - no file yet, that's fine.
        return []
    except json.JSONDecodeError:
        print("Warning: data file is corrupted or empty. Starting with an empty list.")
        return []
    except OSError as e:
        print(f"Warning: could not read the data file ({e}). Starting with an empty list.")
        return []


def save_records(records):
    """Save the current list of records to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except OSError as e:
        print(f"Error: could not save records to file ({e}). Your changes may be lost on exit.")

def find_student_by_id(records, student_id):
    """Return the student dictionary with the matching ID, or None if not found."""
    for student in records:
        if student["id"] == student_id:
            return student
    return None

def display_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("==============================================")

def add_record(records):
    print("\n--- Add New Student Record ---")

    student_id = input("Enter Student ID: ").strip()
    if student_id == "":
        print("Student ID cannot be empty. Record not added.")
        return

    if find_student_by_id(records, student_id) is not None:
        print(f"A student with ID '{student_id}' already exists. Record not added.")
        return

    name = input("Enter Name: ").strip()
    if name == "":
        print("Name cannot be empty. Record not added.")
        return

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Age must be a positive number. Record not added.")
            return
    except ValueError:
        print("Age must be a number. Record not added.")
        return

    course = input("Enter Course: ").strip()

    email = input("Enter Email: ").strip()
    if email == "":
        print("Email cannot be empty. Record not added.")
        return

    phone = input("Enter Phone: ").strip()

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone
    }

    records.append(new_student)
    save_records(records)
    print(f"Student '{name}' added successfully.")


def view_records(records):
    print("\n--- All Student Records ---")

    if len(records) == 0:
        print("No records found.")
        return

    for student in records:
        print("-" * 40)
        print(f"Student ID : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Course     : {student['course']}")
        print(f"Email      : {student['email']}")
        print(f"Phone      : {student['phone']}")
    print("-" * 40)


def search_record(records):
    print("\n--- Search Student Record ---")
    student_id = input("Enter Student ID to search: ").strip()

    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"No student found with ID '{student_id}'.")
        return

    print("-" * 40)
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")
    print(f"Email      : {student['email']}")
    print(f"Phone      : {student['phone']}")
    print("-" * 40)


def update_record(records):
    print("\n--- Update Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()

    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"No student found with ID '{student_id}'.")
        return

    print(f"Found student: {student['name']}")
    print("Which field do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Course")
    print("4. Email")
    print("5. Phone")

    try:
        field_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Update cancelled.")
        return

    if field_choice == 1:
        new_name = input("Enter new Name: ").strip()
        if new_name == "":
            print("Name cannot be empty. Update cancelled.")
            return
        student["name"] = new_name

    elif field_choice == 2:
        try:
            new_age = int(input("Enter new Age: "))
            if new_age <= 0:
                print("Age must be a positive number. Update cancelled.")
                return
        except ValueError:
            print("Age must be a number. Update cancelled.")
            return
        student["age"] = new_age

    elif field_choice == 3:
        student["course"] = input("Enter new Course: ").strip()

    elif field_choice == 4:
        new_email = input("Enter new Email: ").strip()
        if new_email == "":
            print("Email cannot be empty. Update cancelled.")
            return
        student["email"] = new_email

    elif field_choice == 5:
        student["phone"] = input("Enter new Phone: ").strip()

    else:
        print("Invalid field choice. Update cancelled.")
        return

    save_records(records)
    print("Record updated successfully.")


def delete_record(records):
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()

    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"No student found with ID '{student_id}'.")
        return

    confirm = input(f"Are you sure you want to delete '{student['name']}' (ID: {student_id})? (y/n): ").strip().lower()

    if confirm == "y":
        records.remove(student)
        save_records(records)
        print("Record deleted successfully.")
    else:
        print("Delete cancelled.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():
    records = load_records()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_record(records)
        elif choice == 2:
            view_records(records)
        elif choice == 3:
            search_record(records)
        elif choice == 4:
            update_record(records)
        elif choice == 5:
            delete_record(records)
        elif choice == 6:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
