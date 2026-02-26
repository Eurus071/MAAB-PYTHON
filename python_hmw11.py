import sqlite3
import os
from typing import List, Tuple, Any

# ============================================================================
# TASK 1: ROSTER MANAGEMENT DATABASE
# ============================================================================

class RosterManager:
    """Manage the Roster database for Task 1"""
    
    def __init__(self, db_name='roster.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Connect to the database"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f" Connected to {self.db_name}")
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print(f" Closed connection to {self.db_name}")
    
    def create_table(self):
        """Create the Roster table"""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Roster (
                    Name TEXT NOT NULL,
                    Species TEXT NOT NULL,
                    Age INTEGER NOT NULL
                )
            ''')
            self.conn.commit()
            print(" Created Roster table")
        except sqlite3.Error as e:
            print(f" Error creating table: {e}")
    
    def insert_initial_data(self):
        """Insert initial data into Roster table"""
        characters = [
            ('Benjamin Sisko', 'Human', 40),
            ('Jadzia Dax', 'Trill', 300),
            ('Kira Nerys', 'Bajoran', 29)
        ]
        
        try:
            self.cursor.executemany('''
                INSERT INTO Roster (Name, Species, Age) 
                VALUES (?, ?, ?)
            ''', characters)
            self.conn.commit()
            print(f" Inserted {len(characters)} characters")
        except sqlite3.Error as e:
            print(f" Error inserting data: {e}")
    
    def update_jadzia_to_ezri(self):
        try:
            self.cursor.execute('''
                UPDATE Roster 
                SET Name = 'Ezri Dax' 
                WHERE Name = 'Jadzia Dax'
            ''')
            self.conn.commit()
            print(" Updated Jadzia Dax to Ezri Dax")
        except sqlite3.Error as e:
            print(f" Error updating data: {e}")
    
    def query_bajorans(self):
        """Query all Bajoran characters"""
        try:
            self.cursor.execute('''
                SELECT Name, Age 
                FROM Roster 
                WHERE Species = 'Bajoran'
            ''')
            results = self.cursor.fetchall()
            
            print("\n Bajoran Characters:")
            print("-" * 30)
            if results:
                for name, age in results:
                    print(f"Name: {name}, Age: {age}")
            else:
                print("No Bajoran characters found")
            return results
        except sqlite3.Error as e:
            print(f" Error querying data: {e}")
            return []
    
    def delete_over_100_years(self):
        """Delete characters over 100 years old"""
        try:
            self.cursor.execute('''
                DELETE FROM Roster 
                WHERE Age > 100
            ''')
            deleted_count = self.cursor.rowcount
            self.conn.commit()
            print(f" Deleted {deleted_count} character(s) over 100 years old")
            return deleted_count
        except sqlite3.Error as e:
            print(f" Error deleting data: {e}")
            return 0
    
    def add_rank_column(self):
        """Add Rank column and populate data"""
        try:
            # Add Rank column
            self.cursor.execute('''
                ALTER TABLE Roster 
                ADD COLUMN Rank TEXT
            ''')
            print(" Added Rank column")
            
            # Update Rank values
            rank_updates = [
                ('Captain', 'Benjamin Sisko'),
                ('Lieutenant', 'Ezri Dax'),
                ('Major', 'Kira Nerys')
            ]
            
            for rank, name in rank_updates:
                self.cursor.execute('''
                    UPDATE Roster 
                    SET Rank = ? 
                    WHERE Name = ?
                ''', (rank, name))
            
            self.conn.commit()
            print(" Updated Rank values")
        except sqlite3.Error as e:
            # Column might already exist
            if "duplicate column name" in str(e):
                print("  Rank column already exists, updating values...")
                # Update Rank values anyway
                rank_updates = [
                    ('Captain', 'Benjamin Sisko'),
                    ('Lieutenant', 'Ezri Dax'),
                    ('Major', 'Kira Nerys')
                ]
                
                for rank, name in rank_updates:
                    self.cursor.execute('''
                        UPDATE Roster 
                        SET Rank = ? 
                        WHERE Name = ?
                    ''', (rank, name))
                
                self.conn.commit()
                print(" Updated Rank values")
            else:
                print(f" Error adding Rank column: {e}")
    
    def query_sorted_by_age(self):
        """Query all characters sorted by age descending"""
        try:
            self.cursor.execute('''
                SELECT Name, Species, Age, Rank 
                FROM Roster 
                ORDER BY Age DESC
            ''')
            results = self.cursor.fetchall()
            
            print("\n Characters Sorted by Age (Descending):")
            print("-" * 50)
            print(f"{'Name':<20} {'Species':<10} {'Age':<5} {'Rank':<12}")
            print("-" * 50)
            
            if results:
                for name, species, age, rank in results:
                    rank_display = rank if rank else "N/A"
                    print(f"{name:<20} {species:<10} {age:<5} {rank_display:<12}")
            else:
                print("No characters found")
            return results
        except sqlite3.Error as e:
            print(f" Error querying sorted data: {e}")
            return []
    
    def display_all_roster(self):
        """Display all data in Roster table"""
        try:
            self.cursor.execute('SELECT * FROM Roster')
            results = self.cursor.fetchall()
            
            print("\n Complete Roster:")
            print("-" * 50)
            print(f"{'Name':<20} {'Species':<10} {'Age':<5} {'Rank':<12}")
            print("-" * 50)
            
            if results:
                for row in results:
                    name, species, age, rank = row if len(row) == 4 else (*row, "N/A")
                    print(f"{name:<20} {species:<10} {age:<5} {rank:<12}")
            else:
                print("No data in Roster table")
        except sqlite3.Error as e:
            print(f" Error displaying roster: {e}")
    
    def run_all_tasks(self):
        """Run all tasks for roster management"""
        print("=" * 60)
        print("TASK 1: ROSTER MANAGEMENT DATABASE")
        print("=" * 60)
        
        try:
            # Connect to database
            self.connect()
            
            # 1. Create table
            print("\n Creating Roster table...")
            self.create_table()
            
            # 2. Insert initial data
            print("\n Inserting initial data...")
            self.insert_initial_data()
            self.display_all_roster()
            
            # 3. Update Jadzia to Ezri
            print("\n Updating Jadzia Dax to Ezri Dax...")
            self.update_jadzia_to_ezri()
            self.display_all_roster()
            
            # 4. Query Bajoran characters
            print("\n Querying Bajoran characters...")
            self.query_bajorans()
            
            # 5. Delete characters over 100 years
            print("\n Deleting characters over 100 years old...")
            self.delete_over_100_years()
            self.display_all_roster()
            
            # 6. Bonus: Add Rank column
            print("\n Bonus: Adding Rank column...")
            self.add_rank_column()
            self.display_all_roster()
            
            # 7. Advanced query: Sort by age
            print("\n Advanced query: Sorting by age descending...")
            self.query_sorted_by_age()
            
        finally:
            # Close connection
            self.close()

# ============================================================================
# TASK 2: LIBRARY MANAGEMENT DATABASE
# ============================================================================

class LibraryManager:
    """Manage the Library database for Task 2"""
    
    def __init__(self, db_name='library.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Connect to the database"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f" Connected to {self.db_name}")
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print(f" Closed connection to {self.db_name}")
    
    def create_table(self):
        """Create the Books table"""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Books (
                    Title TEXT NOT NULL,
                    Author TEXT NOT NULL,
                    Year_Published INTEGER NOT NULL,
                    Genre TEXT NOT NULL
                )
            ''')
            self.conn.commit()
            print(" Created Books table")
        except sqlite3.Error as e:
            print(f" Error creating table: {e}")
    
    def insert_initial_data(self):
        """Insert initial data into Books table"""
        books = [
            ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
            ('1984', 'George Orwell', 1949, 'Dystopian'),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
        ]
        
        try:
            self.cursor.executemany('''
                INSERT INTO Books (Title, Author, Year_Published, Genre) 
                VALUES (?, ?, ?, ?)
            ''', books)
            self.conn.commit()
            print(f" Inserted {len(books)} books")
        except sqlite3.Error as e:
            print(f" Error inserting data: {e}")
    
    def update_1984_year(self):
        """Update 1984 year published to 1950"""
        try:
            self.cursor.execute('''
                UPDATE Books 
                SET Year_Published = 1950 
                WHERE Title = '1984'
            ''')
            self.conn.commit()
            print(" Updated 1984 year published to 1950")
        except sqlite3.Error as e:
            print(f" Error updating data: {e}")
    
    def query_dystopian_books(self):
        """Query all Dystopian books"""
        try:
            self.cursor.execute('''
                SELECT Title, Author 
                FROM Books 
                WHERE Genre = 'Dystopian'
            ''')
            results = self.cursor.fetchall()
            
            print("\n Dystopian Books:")
            print("-" * 40)
            if results:
                for title, author in results:
                    print(f"Title: {title}, Author: {author}")
            else:
                print("No Dystopian books found")
            return results
        except sqlite3.Error as e:
            print(f" Error querying data: {e}")
            return []
    
    def delete_pre_1950_books(self):
        """Delete books published before 1950"""
        try:
            self.cursor.execute('''
                DELETE FROM Books 
                WHERE Year_Published < 1950
            ''')
            deleted_count = self.cursor.rowcount
            self.conn.commit()
            print(f" Deleted {deleted_count} book(s) published before 1950")
            return deleted_count
        except sqlite3.Error as e:
            print(f" Error deleting data: {e}")
            return 0
    
    def add_rating_column(self):
        """Add Rating column and populate data"""
        try:
            # Add Rating column
            self.cursor.execute('''
                ALTER TABLE Books 
                ADD COLUMN Rating REAL
            ''')
            print(" Added Rating column")
            
            # Update Rating values
            rating_updates = [
                (4.8, 'To Kill a Mockingbird'),
                (4.7, '1984'),
                (4.5, 'The Great Gatsby')
            ]
            
            for rating, title in rating_updates:
                self.cursor.execute('''
                    UPDATE Books 
                    SET Rating = ? 
                    WHERE Title = ?
                ''', (rating, title))
            
            self.conn.commit()
            print(" Updated Rating values")
        except sqlite3.Error as e:
            # Column might already exist
            if "duplicate column name" in str(e):
                print("  Rating column already exists, updating values...")
                # Update Rating values anyway
                rating_updates = [
                    (4.8, 'To Kill a Mockingbird'),
                    (4.7, '1984'),
                    (4.5, 'The Great Gatsby')
                ]
                
                for rating, title in rating_updates:
                    self.cursor.execute('''
                        UPDATE Books 
                        SET Rating = ? 
                        WHERE Title = ?
                    ''', (rating, title))
                
                self.conn.commit()
                print(" Updated Rating values")
            else:
                print(f" Error adding Rating column: {e}")
    
    def query_sorted_by_year(self):
        """Query all books sorted by year published ascending"""
        try:
            self.cursor.execute('''
                SELECT Title, Author, Year_Published, Genre, Rating 
                FROM Books 
                ORDER BY Year_Published ASC
            ''')
            results = self.cursor.fetchall()
            
            print("\n Books Sorted by Year Published (Ascending):")
            print("-" * 70)
            print(f"{'Title':<25} {'Author':<20} {'Year':<6} {'Genre':<12} {'Rating':<6}")
            print("-" * 70)
            
            if results:
                for title, author, year, genre, rating in results:
                    rating_display = f"{rating:.1f}" if rating is not None else "N/A"
                    print(f"{title:<25} {author:<20} {year:<6} {genre:<12} {rating_display:<6}")
            else:
                print("No books found")
            return results
        except sqlite3.Error as e:
            print(f" Error querying sorted data: {e}")
            return []
    
    def display_all_books(self):
        """Display all data in Books table"""
        try:
            self.cursor.execute('SELECT * FROM Books')
            results = self.cursor.fetchall()
            
            print("\n Complete Library:")
            print("-" * 70)
            
            # Check if Rating column exists
            self.cursor.execute("PRAGMA table_info(Books)")
            columns = self.cursor.fetchall()
            has_rating = any(col[1] == 'Rating' for col in columns)
            
            if has_rating:
                print(f"{'Title':<25} {'Author':<20} {'Year':<6} {'Genre':<12} {'Rating':<6}")
                print("-" * 70)
                for row in results:
                    title, author, year, genre, rating = row if len(row) == 5 else (*row, None)
                    rating_display = f"{rating:.1f}" if rating is not None else "N/A"
                    print(f"{title:<25} {author:<20} {year:<6} {genre:<12} {rating_display:<6}")
            else:
                print(f"{'Title':<25} {'Author':<20} {'Year':<6} {'Genre':<12}")
                print("-" * 70)
                for row in results:
                    title, author, year, genre = row
                    print(f"{title:<25} {author:<20} {year:<6} {genre:<12}")
        except sqlite3.Error as e:
            print(f" Error displaying books: {e}")
    
    def add_sample_books(self):
        """Add additional sample books for better demonstration"""
        additional_books = [
            ('Brave New World', 'Aldous Huxley', 1932, 'Dystopian', 4.2),
            ('Fahrenheit 451', 'Ray Bradbury', 1953, 'Dystopian', 4.3),
            ('Pride and Prejudice', 'Jane Austen', 1813, 'Classic', 4.7),
            ('Moby Dick', 'Herman Melville', 1851, 'Classic', 3.8),
            ('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction', 4.0),
            ('Animal Farm', 'George Orwell', 1945, 'Dystopian', 4.5)
        ]
        
        try:
            # Check if Rating column exists
            self.cursor.execute("PRAGMA table_info(Books)")
            columns = self.cursor.fetchall()
            has_rating = any(col[1] == 'Rating' for col in columns)
            
            if has_rating:
                self.cursor.executemany('''
                    INSERT INTO Books (Title, Author, Year_Published, Genre, Rating) 
                    VALUES (?, ?, ?, ?, ?)
                ''', additional_books)
            else:
                # Insert without rating
                books_no_rating = [(b[0], b[1], b[2], b[3]) for b in additional_books]
                self.cursor.executemany('''
                    INSERT INTO Books (Title, Author, Year_Published, Genre) 
                    VALUES (?, ?, ?, ?)
                ''', books_no_rating)
            
            self.conn.commit()
            print(f" Added {len(additional_books)} additional sample books")
        except sqlite3.Error as e:
            print(f" Error adding sample books: {e}")
    
    def run_all_tasks(self):
        """Run all tasks for library management"""
        print("=" * 60)
        print("TASK 2: LIBRARY MANAGEMENT DATABASE")
        print("=" * 60)
        
        try:
            # Connect to database
            self.connect()
            
            # 1. Create table
            print("\n Creating Books table...")
            self.create_table()
            
            # 2. Insert initial data
            print("\n Inserting initial data...")
            self.insert_initial_data()
            self.display_all_books()
            
            # 3. Update 1984 year
            print("\n Updating 1984 year published to 1950...")
            self.update_1984_year()
            self.display_all_books()
            
            # 4. Query Dystopian books
            print("\n Querying Dystopian books...")
            self.query_dystopian_books()
            
            # 5. Delete books before 1950
            print("\n Deleting books published before 1950...")
            self.delete_pre_1950_books()
            self.display_all_books()
            
            # 6. Bonus: Add Rating column
            print("\n Bonus: Adding Rating column...")
            self.add_rating_column()
            
            print("\n Adding more sample books for demonstration...")
            self.add_sample_books()
            
            self.display_all_books()
            
            print("\n Advanced query: Sorting by year published ascending...")
            self.query_sorted_by_year()
            
            print("\n Additional Statistics:")
            print("-" * 40)
            
            self.cursor.execute('''
                SELECT Genre, COUNT(*) as Count, AVG(Rating) as AvgRating
                FROM Books 
                GROUP BY Genre
                ORDER BY Count DESC
            ''')
            genre_stats = self.cursor.fetchall()
            
            print("\nBooks by Genre:")
            for genre, count, avg_rating in genre_stats:
                avg_display = f"{avg_rating:.2f}" if avg_rating is not None else "N/A"
                print(f"  {genre}: {count} books, Avg Rating: {avg_display}")
            
            self.cursor.execute('SELECT MIN(Year_Published), MAX(Year_Published) FROM Books')
            min_year, max_year = self.cursor.fetchone()
            print(f"\nPublication Years: {min_year} to {max_year}")
            
        finally:
            self.close()

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def cleanup_databases():
    """Remove existing database files"""
    for db_file in ['roster.db', 'library.db']:
        if os.path.exists(db_file):
            try:
                os.remove(db_file)
                print(f" Removed existing {db_file}")
            except OSError as e:
                print(f" Could not remove {db_file}: {e}")

def run_database_exploration():
    """Interactive exploration of created databases"""
    print("\n" + "=" * 60)
    print("DATABASE EXPLORATION")
    print("=" * 60)
    
    while True:
        print("\nWhich database would you like to explore?")
        print("1. Roster Database (roster.db)")
        print("2. Library Database (library.db)")
        print("3. Run custom SQL query")
        print("4. Return to main menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            explore_database('roster.db')
        elif choice == '2':
            explore_database('library.db')
        elif choice == '3':
            run_custom_query()
        elif choice == '4':
            break
        else:
            print(" Invalid choice. Please try again.")

def explore_database(db_name):
    """Explore a specific database"""
    if not os.path.exists(db_name):
        print(f" Database {db_name} does not exist")
        return
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print(f"\nExploring {db_name}:")
        print("-" * 40)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        if not tables:
            print("No tables found in database")
            return
        
        for table_name, in tables:
            print(f"\n Table: {table_name}")
            print("-" * 30)
            
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            
            print("Columns:")
            for col in columns:
                col_id, col_name, col_type, not_null, default_val, pk = col
                print(f"  {col_name} ({col_type})")
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            print(f"\nTotal rows: {row_count}")
            if row_count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
                rows = cursor.fetchall()
                
                print("\nSample data:")
                for row in rows:
                    print(f"  {row}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f" Error exploring database: {e}")

def run_custom_query():
    """Run a custom SQL query"""
    print("\n" + "=" * 60)
    print("CUSTOM SQL QUERY")
    print("=" * 60)
    
    print("\nWhich database would you like to query?")
    print("1. roster.db")
    print("2. library.db")
    
    db_choice = input("\nEnter choice (1-2): ").strip()
    
    if db_choice == '1':
        db_name = 'roster.db'
    elif db_choice == '2':
        db_name = 'library.db'
    else:
        print(" Invalid choice")
        return
    
    if not os.path.exists(db_name):
        print(f" Database {db_name} does not exist")
        return
    
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print(f"\n Example queries for {db_name}:")
        if db_name == 'roster.db':
            print("  SELECT * FROM Roster")
            print("  SELECT Name, Age FROM Roster WHERE Species = 'Human'")
            print("  SELECT * FROM Roster ORDER BY Age DESC")
        else:
            print("  SELECT * FROM Books")
            print("  SELECT Title, Author FROM Books WHERE Rating > 4.5")
            print("  SELECT Genre, COUNT(*) FROM Books GROUP BY Genre")
        
        print("\nEnter your SQL query (or 'exit' to quit):")
        
        while True:
            query = input("\nSQL> ").strip()
            
            if query.lower() == 'exit':
                break
            elif not query:
                continue
            
            try:
                cursor.execute(query)
                if query.strip().upper().startswith('SELECT'):
                    results = cursor.fetchall()
                    
                    if results:
                        column_names = [description[0] for description in cursor.description]
                        print("\nResults:")
                        print("-" * 80)
                        header = " | ".join(str(name).ljust(20) for name in column_names)
                        print(header)
                        print("-" * 80)
                        for row in results:
                            row_str = " | ".join(str(value).ljust(20) for value in row)
                            print(row_str)
                        
                        print(f"\nTotal rows: {len(results)}")
                    else:
                        print("No results found")
                else:
                    # For non-SELECT queries (INSERT, UPDATE, DELETE)
                    conn.commit()
                    print(f" Query executed successfully. Rows affected: {cursor.rowcount}")
            
            except sqlite3.Error as e:
                print(f" SQL Error: {e}")
            except Exception as e:
                print(f" Error: {e}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f" Error connecting to database: {e}")

def main():
    """Main application menu"""
    print("=" * 70)
    print("SQLITE DATABASE MANAGEMENT SYSTEM")
    print("=" * 70)
    print("\n Cleaning up old database files...")
    cleanup_databases()
    
    while True:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1.  Run Task 1: Roster Management")
        print("2.  Run Task 2: Library Management")
        print("3.  Run Both Tasks")
        print("4.  Explore Databases")
        print("5.  Run Custom SQL Queries")
        print("6.  Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # Run Task 1
            roster_manager = RosterManager()
            roster_manager.run_all_tasks()
            
        elif choice == '2':
            # Run Task 2
            library_manager = LibraryManager()
            library_manager.run_all_tasks()
            
        elif choice == '3':
            print("\n" + "=" * 70)
            print("RUNNING BOTH DATABASE TASKS")
            print("=" * 70)
            
            print("\n Starting Task 1: Roster Management...")
            roster_manager = RosterManager()
            roster_manager.run_all_tasks()
            
            input("\n Press Enter to continue to Task 2...")
            
            print("\n Starting Task 2: Library Management...")
            library_manager = LibraryManager()
            library_manager.run_all_tasks()
            
            print("\n" + "=" * 70)
            print("BOTH TASKS COMPLETED SUCCESSFULLY!")
            print("=" * 70)
            
        elif choice == '4':
            run_database_exploration()
            
        elif choice == '5':
            run_custom_query()
            
        elif choice == '6':
            print("\n" + "=" * 60)
            print("Thank you for using the Database Management System!")
            print("=" * 60)
            break
        
        else:
            print(" Invalid choice. Please try again.")


def quick_demo():
    """Run a quick demonstration of both tasks"""
    print("=" * 70)
    print("QUICK DATABASE DEMONSTRATION")
    print("=" * 70)

    cleanup_databases()
    
    print("\n Task 1: Roster Management")
    print("-" * 40)
    
    # Task 1
    roster = RosterManager()
    roster.connect()
    roster.create_table()
    roster.insert_initial_data()
    roster.update_jadzia_to_ezri()
    print("\nAfter updates:")
    roster.display_all_roster()
    roster.close()
    
    print("\n Task 2: Library Management")
    print("-" * 40)
    
    # Task 2
    library = LibraryManager()
    library.connect()
    library.create_table()
    library.insert_initial_data()
    library.update_1984_year()
    print("\nAfter updates:")
    library.display_all_books()
    library.close()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)
    print("\nDatabases created:")
    print("  - roster.db (Roster Management)")
    print("  - library.db (Library Management)")
    print("\nRun the main() function for full interactive experience.")

if __name__ == "__main__":
    print("Welcome to the SQLite Database Management System!")
    print("\nChoose mode:")
    print("1. Run main application (interactive)")
    print("2. Run quick demonstration")
    
    mode = input("\nEnter choice (1 or 2): ").strip()
    
    if mode == '2':
        quick_demo()
    else:
        main()