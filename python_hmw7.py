import math
import os
import json
import csv

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    # Addition
    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    # Subtraction
    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    # Dot product OR scalar multiplication
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported multiplication")

    # Allow scalar * vector
    def __rmul__(self, scalar):
        return self * scalar

    # Magnitude
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    # Normalize
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        normalized = [round(a / mag, 3) for a in self.components]
        return Vector(*normalized)

#####     import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    # Read all employees from file
    def load_employees(self):
        employees = []
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 4:
                    employees.append(Employee(*parts))
        return employees

    # Save all employees to file
    def save_employees(self, employees):
        with open(self.filename, "w") as file:
            for emp in employees:
                file.write(str(emp) + "\n")

    # Check unique ID
    def id_exists(self, emp_id):
        for emp in self.load_employees():
            if emp.employee_id == emp_id:
                return True
        return False

    # Option 1
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if self.id_exists(emp_id):
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        emp = Employee(emp_id, name, position, salary)
        with open(self.filename, "a") as file:
            file.write(str(emp) + "\n")

        print("Employee added successfully!")

    # Option 2
    def view_all(self):
        employees = self.load_employees()
        if not employees:
            print("No employee records found.")
            return

        print("\nEmployee Records:")
        for emp in employees:
            print(emp)

    # Option 3
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for emp in self.load_employees():
            if emp.employee_id == emp_id:
                print("\nEmployee Found:")
                print(emp)
                return
        print("Employee not found.")

    # Option 4
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        employees = self.load_employees()
        found = False

        for emp in employees:
            if emp.employee_id == emp_id:
                print("Leave blank to keep old value.")
                name = input(f"New Name ({emp.name}): ") or emp.name
                position = input(f"New Position ({emp.position}): ") or emp.position
                salary = input(f"New Salary ({emp.salary}): ") or emp.salary

                emp.name = name
                emp.position = position
                emp.salary = salary
                found = True
                break

        if found:
            self.save_employees(employees)
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    # Option 5
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        employees = self.load_employees()
        new_list = [emp for emp in employees if emp.employee_id != emp_id]

        if len(new_list) == len(employees):
            print("Employee not found.")
        else:
            self.save_employees(new_list)
            print("Employee deleted successfully!")

    # Menu
    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()



### import json
### import csv


# ---------------- STORAGE LAYER ----------------

class StorageBase:
    def save(self, tasks):
        pass

    def load(self):
        pass


class JSONStorage(StorageBase):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump(tasks, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)


class CSVStorage(StorageBase):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        tasks = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(row)
        return tasks


# ---------------- TASK MANAGER ----------------

class TodoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        task = {
            "id": input("Enter Task ID: "),
            "title": input("Enter Title: "),
            "description": input("Enter Description: "),
            "due_date": input("Enter Due Date (YYYY-MM-DD): "),
            "status": input("Enter Status (Pending/In Progress/Completed): ")
        }
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTasks:")
        for t in self.tasks:
            print(f"{t['id']}, {t['title']}, {t['description']}, {t['due_date']}, {t['status']}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = input("New Title: ") or task["title"]
                task["description"] = input("New Description: ") or task["description"]
                task["due_date"] = input("New Due Date: ") or task["due_date"]
                task["status"] = input("New Status: ") or task["status"]
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter by: ")
        filtered = [t for t in self.tasks if t["status"].lower() == status.lower()]
        for t in filtered:
            print(f"{t['id']}, {t['title']}, {t['status']}")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    # Change here to switch format with minimal code change:
    storage = JSONStorage()     # or CSVStorage()

    app = TodoApp(storage)
    app.menu()
