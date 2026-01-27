import json
import csv
import os
from datetime import datetime

# ============================================================================
# TASK 1: LIBRARY MANAGEMENT SYSTEM WITH CUSTOM EXCEPTIONS
# ============================================================================

class BookNotFoundException(Exception):
    """Raised when trying to borrow a book that doesn't exist"""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when a book is already borrowed"""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more books than allowed"""
    pass

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None
    
    def borrow(self, member_name, days=14):
        """Mark book as borrowed"""
        self.is_borrowed = True
        self.borrowed_by = member_name
        self.due_date = datetime.now().date().isoformat()
    
    def return_book(self):
        """Mark book as returned"""
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        if self.is_borrowed:
            return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status} by {self.borrowed_by}"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  
        self.max_books = 3  
    
    def can_borrow_more(self):
        """Check if member can borrow more books"""
        return len(self.borrowed_books) < self.max_books
    
    def borrow_book(self, book):
        """Add book to member's borrowed list"""
        if len(self.borrowed_books) >= self.max_books:
            raise MemberLimitExceededException(
                f"{self.name} has reached the limit of {self.max_books} books"
            )
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        """Remove book from member's borrowed list"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}), Books borrowed: {len(self.borrowed_books)}/{self.max_books}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {} 
        self.members = {} 
        self.next_member_id = 1001
    
    def add_book(self, title, author, isbn):
        """Add a new book to the library"""
        book = Book(title, author, isbn)
        self.books[isbn] = book
        print(f"Added book: '{title}'")
        return book
    
    def add_member(self, name):
        """Add a new member to the library"""
        member_id = f"M{self.next_member_id}"
        member = Member(name, member_id)
        self.members[member_id] = member
        self.next_member_id += 1
        print(f"Added member: {name} (ID: {member_id})")
        return member
    
    def borrow_book(self, isbn, member_id):
        """Borrow a book from the library"""
    
        if isbn not in self.books:
            raise BookNotFoundException(f"Book with ISBN {isbn} not found in library")
        
        book = self.books[isbn]
        
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"Book '{book.title}' is already borrowed by {book.borrowed_by}"
            )
        
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} not found")
        
        member = self.members[member_id]
        
        if not member.can_borrow_more():
            raise MemberLimitExceededException(
                f"{member.name} has reached the borrowing limit of {member.max_books} books"
            )
        
        book.borrow(member.name)
        member.borrow_book(book)
        print(f"{member.name} successfully borrowed '{book.title}'")
        return True
    
    def return_book(self, isbn):
        """Return a book to the library"""
        if isbn not in self.books:
            raise BookNotFoundException(f"Book with ISBN {isbn} not found in library")
        
        book = self.books[isbn]
        
        if not book.is_borrowed:
            print(f"Book '{book.title}' was not borrowed")
            return False
        member_name = book.borrowed_by
        for member in self.members.values():
            if member.name == member_name:
                member.return_book(book)
                break
        
        book.return_book()
        print(f"Book '{book.title}' has been returned")
        return True
    
    def display_books(self):
        """Display all books in the library"""
        print("\n" + "=" * 60)
        print(f"BOOKS IN {self.name.upper()} LIBRARY")
        print("=" * 60)
        if not self.books:
            print("No books available")
        else:
            for book in self.books.values():
                print(f"  - {book}")
    
    def display_members(self):
        """Display all library members"""
        print("\n" + "=" * 60)
        print("LIBRARY MEMBERS")
        print("=" * 60)
        if not self.members:
            print("No members registered")
        else:
            for member in self.members.values():
                print(f"  - {member}")
                if member.borrowed_books:
                    print("    Borrowed books:")
                    for book in member.borrowed_books:
                        print(f"      • {book.title}")

def test_library_system():
    """Test the library management system"""
    print("=" * 60)
    print("TESTING LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    library = Library("City Library")
  
    print("\n--- Adding Books ---")
    books_data = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
        ("To Kill a Mockingbird", "Harper Lee", "9780446310789"),
        ("1984", "George Orwell", "9780451524935"),
        ("Pride and Prejudice", "Jane Austen", "9780141439518"),
    ]
    
    for title, author, isbn in books_data:
        library.add_book(title, author, isbn)
   
    print("\n--- Adding Members ---")
    members = ["Alice Johnson", "Bob Smith", "Carol Davis"]
    for member_name in members:
        library.add_member(member_name)
    
    library.display_books()
    library.display_members()
    
  
    print("\n--- Testing Book Borrowing ---")
    try:
        library.borrow_book("9780743273565", "M1001")  
        library.borrow_book("9780446310789", "M1002")  
        
     
        print("\nTrying to borrow already borrowed book:")
        library.borrow_book("9780743273565", "M1003")  
    except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(f"Exception caught: {e}")

    print("\nTrying to borrow non-existent book:")
    try:
        library.borrow_book("9999999999999", "M1001")
    except BookNotFoundException as e:
        print(f"Exception caught: {e}")
    

    print("\nTesting member borrowing limit:")
    try:
     
        library.borrow_book("9780451524935", "M1001") 
        library.borrow_book("9780141439518", "M1001")  
     
        library.borrow_book("9780446310789", "M1001")  
    except MemberLimitExceededException as e:
        print(f"Exception caught: {e}")
    

    print("\n--- Current Library Status ---")
    library.display_books()
    library.display_members()
    
  
    print("\n--- Testing Book Returns ---")
    library.return_book("9780743273565") 
    library.return_book("9999999999999")  
    

    print("\n--- Final Library Status ---")
    library.display_books()
    library.display_members()

# ============================================================================
# TASK 2: STUDENT GRADES MANAGEMENT
# ============================================================================

def create_grades_csv():
    """Create the initial grades.csv file"""
    data = [
        ["Name", "Subject", "Grade"],
        ["Alice", "Math", 85],
        ["Bob", "Science", 78],
        ["Carol", "Math", 92],
        ["Dave", "History", 74],
        ["Eve", "Science", 88],
        ["Frank", "Math", 79],
        ["Grace", "History", 91],
        ["Henry", "Science", 82],
    ]
    
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Created grades.csv file")

def manage_student_grades():
    """Read, process, and write grade data"""
    print("\n" + "=" * 60)
    print("STUDENT GRADES MANAGEMENT")
    print("=" * 60)
    

    print("\n--- Reading grades.csv ---")
    students = []
    
    try:
        with open('grades.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
   
                row['Grade'] = int(row['Grade'])
                students.append(row)
        
        print(f"Read {len(students)} student records")
        
   
        print("\nStudent Grades:")
        print("-" * 40)
        for student in students:
            print(f"{student['Name']:10} | {student['Subject']:10} | {student['Grade']:3}")
    
    except FileNotFoundError:
        print("grades.csv not found. Creating sample data...")
        create_grades_csv()
        return manage_student_grades()

    print("\n--- Calculating Average Grades ---")
    subject_grades = {}
    
    for student in students:
        subject = student['Subject']
        grade = student['Grade']
        
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(grade)
    

    averages = []
    for subject, grades in subject_grades.items():
        avg_grade = sum(grades) / len(grades)
        averages.append({
            'Subject': subject,
            'Average Grade': round(avg_grade, 2)
        })
        print(f"{subject}: {avg_grade:.2f} (from {len(grades)} students)")

    print("\n--- Writing average_grades.csv ---")
    with open('average_grades.csv', 'w', newline='') as file:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(averages)
    
    print("Successfully created average_grades.csv")
    

    print("\nContents of average_grades.csv:")
    print("-" * 40)
    with open('average_grades.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:15} | {row[1]:>15}")

# ============================================================================
# TASK 3: JSON HANDLING
# ============================================================================

def create_tasks_json():
    """Create the initial tasks.json file"""
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1},
        {"id": 4, "task": "Call mom", "completed": False, "priority": 2},
        {"id": 5, "task": "Exercise", "completed": True, "priority": 3},
        {"id": 6, "task": "Read book", "completed": False, "priority": 1},
    ]
    
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)
    print("Created tasks.json file")

def load_and_display_tasks():
    """Load and display tasks from JSON file"""
    print("\n" + "=" * 60)
    print("TASK MANAGEMENT SYSTEM")
    print("=" * 60)
    
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        
        print(f"\nLoaded {len(tasks)} tasks from tasks.json")
   
        print("\nAll Tasks:")
        print("-" * 60)
        print(f"{'ID':<4} {'Task':<25} {'Completed':<10} {'Priority':<8}")
        print("-" * 60)
        
        for task in tasks:
            completed = "✓" if task['completed'] else "✗"
            priority_stars = "★" * task['priority']
            print(f"{task['id']:<4} {task['task']:<25} {completed:<10} {priority_stars:<8}")
        
        return tasks
    
    except FileNotFoundError:
        print("tasks.json not found. Creating sample data...")
        create_tasks_json()
        return load_and_display_tasks()

def calculate_task_stats(tasks):
    """Calculate and display task statistics"""
    print("\n" + "=" * 60)
    print("TASK STATISTICS")
    print("=" * 60)
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    
    if total_tasks > 0:
        total_priority = sum(task['priority'] for task in tasks)
        avg_priority = total_priority / total_tasks
    else:
        avg_priority = 0
    
    print(f"\nTotal Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Completion Rate: {(completed_tasks/total_tasks*100):.1f}%")
    print(f"Average Priority: {avg_priority:.2f}")
    
    # Priority distribution
    print("\nPriority Distribution:")
    priority_counts = {}
    for task in tasks:
        priority = task['priority']
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    for priority in sorted(priority_counts.keys()):
        count = priority_counts[priority]
        bar = "█" * count
        print(f"  Priority {priority}: {bar} ({count})")

def modify_tasks(tasks):
    """Allow user to modify tasks and save changes"""
    print("\n" + "=" * 60)
    print("MODIFY TASKS")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("1. Mark task as completed")
        print("2. Change task priority")
        print("3. Add new task")
        print("4. Save and exit")
        print("5. Exit without saving")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
  
            task_id = input("Enter task ID to mark as completed: ").strip()
            try:
                task_id = int(task_id)
                task_found = False
                for task in tasks:
                    if task['id'] == task_id:
                        task['completed'] = True
                        print(f"Task '{task['task']}' marked as completed!")
                        task_found = True
                        break
                if not task_found:
                    print(f"No task found with ID {task_id}")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '2':

            task_id = input("Enter task ID to change priority: ").strip()
            try:
                task_id = int(task_id)
                priority = input("Enter new priority (1-3): ").strip()
                priority = int(priority)
                
                if 1 <= priority <= 3:
                    task_found = False
                    for task in tasks:
                        if task['id'] == task_id:
                            task['priority'] = priority
                            print(f"Task '{task['task']}' priority changed to {priority}!")
                            task_found = True
                            break
                    if not task_found:
                        print(f"No task found with ID {task_id}")
                else:
                    print("Priority must be between 1 and 3")
            except ValueError:
                print("Please enter valid numbers")
        
        elif choice == '3':
        
            task_name = input("Enter new task name: ").strip()
            if task_name:
       
                max_id = max(task['id'] for task in tasks)
                new_task = {
                    "id": max_id + 1,
                    "task": task_name,
                    "completed": False,
                    "priority": 2 
                }
                tasks.append(new_task)
                print(f"Added new task: '{task_name}' (ID: {max_id + 1})")
        
        elif choice == '4':
          
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=2)
            print("Changes saved to tasks.json")
            break
        
        elif choice == '5':
           
            print("Exiting without saving changes")
            break
        
        else:
            print("Invalid choice. Please try again.")

def convert_json_to_csv(tasks):
    """Convert tasks from JSON to CSV format"""
    print("\n" + "=" * 60)
    print("CONVERTING TASKS TO CSV")
    print("=" * 60)
  
    fieldnames = ['ID', 'Task Name', 'Completed Status', 'Priority']
    
    with open('tasks.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task Name': task['task'],
                'Completed Status': task['completed'],
                'Priority': task['priority']
            })
    
    print("Successfully created tasks.csv")

    print("\nContents of tasks.csv:")
    print("-" * 60)
    with open('tasks.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(f"{row[0]:<4} {row[1]:<25} {row[2]:<15} {row[3]:<8}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all tasks"""
    print("=" * 70)
    print("COMPREHENSIVE PYTHON PROGRAMMING ASSIGNMENT")
    print("=" * 70)
    
    while True:
        print("\nSelect a task to run:")
        print("1. Library Management System (Task 1)")
        print("2. Student Grades Management (Task 2)")
        print("3. JSON Task Management (Task 3)")
        print("4. Run All Tasks")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            test_library_system()
        elif choice == '2':
            manage_student_grades()
        elif choice == '3':

            tasks = load_and_display_tasks()

            calculate_task_stats(tasks)

            convert_json_to_csv(tasks)
        elif choice == '4':
            print("\n" + "=" * 70)
            print("RUNNING ALL TASKS")
            print("=" * 70)
            
            # Task 1
            test_library_system()
            input("\nPress Enter to continue to Task 2...")
            
            # Task 2
            manage_student_grades()
            input("\nPress Enter to continue to Task 3...")
            
            # Task 3
            tasks = load_and_display_tasks()
            calculate_task_stats(tasks)
            convert_json_to_csv(tasks)
            
            print("\n" + "=" * 70)
            print("ALL TASKS COMPLETED SUCCESSFULLY!")
            print("=" * 70)
            print("\nCreated files:")
            print("- grades.csv and average_grades.csv (Task 2)")
            print("- tasks.json and tasks.csv (Task 3)")
        elif choice == '5':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to return to main menu...")

def cleanup_files():
    """Remove generated files (optional - for cleanup)"""
    files_to_remove = ['grades.csv', 'average_grades.csv', 'tasks.json', 'tasks.csv']
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed {file}")

if __name__ == "__main__":

    if not os.path.exists('tasks.json'):
        create_tasks_json()
    if not os.path.exists('grades.csv'):
        create_grades_csv()

    main()