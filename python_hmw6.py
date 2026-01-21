# 1. Zero Check Decorator

def check(func):
    def abc(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return abc

@check
def div(a, b):
    return a / b


print(div(6, 2))
print(div(6, 0))

# 2. Employee Records Manager


FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a") as f:
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully.\n")


def view_employees():
    try:
        with open(FILE_NAME, "r") as f:
            print("\nEmployee Records:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.startswith(emp_id + ","):
                    print("Found:", line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("File not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_lines = []
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                if parts[0] == emp_id:
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    updated_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_lines.append(line)

        with open(FILE_NAME, "w") as f:
            f.writelines(updated_lines)

        if found:
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("File not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    remaining_lines = []
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if not line.startswith(emp_id + ","):
                    remaining_lines.append(line)
                else:
                    found = True

        with open(FILE_NAME, "w") as f:
            f.writelines(remaining_lines)

        if found:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("File not found.")


def employee_menu():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by ID")
        print("4. Update employee information")
        print("5. Delete employee record")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")



employee_menu()


# 3. Word Frequency Counter


import string
from collections import Counter

def create_sample_file():
    text = input("Enter a paragraph to create sample.txt:\n")
    with open("sample.txt", "w") as f:
        f.write(text)


def word_frequency():
    try:
        with open("sample.txt", "r") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print("sample.txt not found.")
        create_sample_file()
        with open("sample.txt", "r") as f:
            text = f.read().lower()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()
    total_words = len(words)

    counter = Counter(words)

    top_n = int(input("How many top common words to display? "))
    common_words = counter.most_common(top_n)

    # Console output
    print("\nTotal words:", total_words)
    print(f"Top {top_n} most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")

    # Save to file
    with open("word_count_report.txt", "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write(f"Top {top_n} Words:\n")
        for word, count in common_words:
            f.write(f"{word} - {count}\n")

    print("\nReport saved to word_count_report.txt")

word_frequency()
