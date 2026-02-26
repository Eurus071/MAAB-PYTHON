import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("PANDAS ADVANCED OPERATIONS - COMPREHENSIVE SOLUTION")
print("=" * 80)

# Create data directory if it doesn't exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# ============================================================================
# PART 1: SETUP AND DATA PREPARATION
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: SETUP AND DATA PREPARATION")
print("=" * 80)

def create_sample_data():
    """Create sample data files for the exercises"""
    
    # 1. Create chinook.db with customers and invoices tables
    print("1. Creating chinook.db with customers and invoices tables...")
    
    conn = sqlite3.connect(data_dir / 'chinook.db')
    cursor = conn.cursor()
    
    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        CustomerId INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Company TEXT,
        Address TEXT,
        City TEXT,
        State TEXT,
        Country TEXT,
        PostalCode TEXT,
        Phone TEXT,
        Fax TEXT,
        Email TEXT,
        SupportRepId INTEGER
    )
    ''')
    
    # Insert customers data
    customers_data = [
        (1, 'Luís', 'Gonçalves', 'Embraer', 'Av. Brigadeiro Faria Lima, 2170', 
         'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', 
         '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3),
        (2, 'Leonie', 'Köhler', None, 'Theodor-Heuss-Straße 34', 
         'Stuttgart', None, 'Germany', '70174', '+49 0711 2842222', 
         None, 'leonekohler@surfeu.de', 5),
        (3, 'François', 'Tremblay', None, '1498 rue Bélanger', 
         'Montréal', 'QC', 'Canada', 'H2G 1A7', '+1 (514) 721-4711', 
         None, 'ftremblay@gmail.com', 3),
        (4, 'Bjørn', 'Hansen', None, 'Ullevålsveien 14', 
         'Oslo', None, 'Norway', '0171', '+47 22 44 22 22', 
         None, 'bjorn.hansen@yahoo.no', 4),
        (5, 'František', 'Wichterlová', 'JetBrains s.r.o.', 
         'Klanova 9/506', 'Prague', None, 'Czech Republic', '14700', 
         '+420 2 4172 5555', '+420 2 4172 5555', 'frantisekw@jetbrains.com', 4)
    ]
    
    cursor.executemany('''
    INSERT OR REPLACE INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', customers_data)
    
    # Create invoices table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        InvoiceId INTEGER PRIMARY KEY,
        CustomerId INTEGER,
        InvoiceDate TEXT,
        BillingAddress TEXT,
        BillingCity TEXT,
        BillingState TEXT,
        BillingCountry TEXT,
        BillingPostalCode TEXT,
        Total REAL,
        FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId)
    )
    ''')
    
    # Insert invoices data
    invoices_data = [
        (1, 1, '2023-01-15', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', 15.99),
        (2, 1, '2023-02-20', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', 25.50),
        (3, 1, '2023-03-10', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', 10.75),
        (4, 2, '2023-01-22', 'Theodor-Heuss-Straße 34', 'Stuttgart', None, 'Germany', '70174', 20.00),
        (5, 2, '2023-03-05', 'Theodor-Heuss-Straße 34', 'Stuttgart', None, 'Germany', '70174', 30.25),
        (6, 3, '2023-02-18', '1498 rue Bélanger', 'Montréal', 'QC', 'Canada', 'H2G 1A7', 12.50),
        (7, 4, '2023-01-30', 'Ullevålsveien 14', 'Oslo', None, 'Norway', '0171', 45.00),
        (8, 4, '2023-03-12', 'Ullevålsveien 14', 'Oslo', None, 'Norway', '0171', 18.75)
    ]
    
    cursor.executemany('''
    INSERT OR REPLACE INTO invoices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', invoices_data)
    
    conn.commit()
    conn.close()
    
    # 2. Create enhanced movie.csv with more columns
    print("2. Creating enhanced movie.csv with additional columns...")
    
    movie_data = {
        'movie_title': [
            'Avatar', 'Titanic', 'The Dark Knight', 'Star Wars: The Force Awakens', 
            'Avengers: Endgame', 'Inception', 'Interstellar', 'The Matrix',
            'Pulp Fiction', 'Forrest Gump', 'The Shawshank Redemption', 'The Godfather',
            'The Wizard of Oz', 'Citizen Kane', 'Casablanca'
        ],
        'director_name': [
            'James Cameron', 'James Cameron', 'Christopher Nolan', 'J.J. Abrams',
            'Anthony Russo', 'Christopher Nolan', 'Christopher Nolan', 'Lana Wachowski',
            'Quentin Tarantino', 'Robert Zemeckis', 'Frank Darabont', 'Francis Ford Coppola',
            'Victor Fleming', 'Orson Welles', 'Michael Curtiz'
        ],
        'color': [
            'Color', 'Color', 'Color', 'Color', 'Color', 'Color', 'Color', 'Color',
            'Color', 'Color', 'Color', 'Color', 'Black and White', 'Black and White', 'Black and White'
        ],
        'duration': [
            162, 195, 152, 138, 181, 148, 169, 136,
            154, 142, 142, 175, 102, 119, 102
        ],
        'director_facebook_likes': [
            0, 0, 21000, 11000, 400, 22000, 23000, 15000,
            18000, 14000, 13000, 16000, 5000, 4000, 3500
        ],
        'num_critic_for_reviews': [
            723, 600, 850, 900, 800, 750, 780, 820,
            890, 700, 880, 850, 500, 520, 480
        ],
        'gross': [
            760505847, 658672302, 533316061, 936662225, 2797800564,
            825532764, 677471339, 463517383, 213928762, 677945399,
            58910109, 245066411, 22240823, 15858537, 96715207
        ],
        'imdb_score': [
            7.9, 7.7, 9.0, 7.9, 8.4, 8.8, 8.6, 8.7,
            8.9, 8.8, 9.3, 9.2, 8.0, 8.3, 8.5
        ]
    }
    
    movie_df = pd.DataFrame(movie_data)
    movie_df.to_csv(data_dir / 'movie.csv', index=False)
    
    # 3. Create employee.csv
    print("3. Creating employee.csv...")
    
    employee_data = {
        'employee_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'name': ['John Smith', 'Jane Doe', 'Bob Johnson', 'Alice Williams', 
                'Charlie Brown', 'Diana Prince', 'Edward Norton', 'Fiona Apple',
                'George Clooney', 'Helen Hunt'],
        'department': ['Sales', 'Sales', 'IT', 'IT', 'Marketing', 
                      'Marketing', 'HR', 'HR', 'Finance', 'Finance'],
        'salary': [50000, 55000, 75000, 82000, 60000, 62000, 48000, 52000, 70000, 75000],
        'years_experience': [5, 6, 8, 10, 4, 5, 3, 4, 7, 8]
    }
    
    employee_df = pd.DataFrame(employee_data)
    employee_df.to_csv(data_dir / 'employee.csv', index=False)
    
    # 4. Create enhanced flights.parquet
    print("4. Creating enhanced flights.parquet...")
    
    flights_data = {
        'Year': [2013, 2013, 2013, 2013, 2013, 2013, 2013, 2013, 2013, 2013],
        'Month': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        'Day': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'DepDelay': [2, 4, 2, -1, -6, 45, 60, -3, 35, 20],
        'ArrDelay': [11, 20, 33, -18, -25, 30, 55, -2, 25, 15],
        'Carrier': ['UA', 'UA', 'AA', 'B6', 'DL', 'UA', 'AA', 'B6', 'DL', 'UA'],
        'Origin': ['EWR', 'LGA', 'JFK', 'JFK', 'LGA', 'EWR', 'JFK', 'LGA', 'EWR', 'JFK'],
        'Dest': ['IAH', 'IAH', 'MIA', 'BQN', 'ATL', 'LAX', 'SFO', 'ORD', 'DFW', 'SEA'],
        'FlightNum': [1545, 1714, 1141, 725, 461, 1589, 1245, 789, 567, 234],
        'TailNum': ['N14228', 'N24211', 'N619AA', 'N804JB', 'N668DN', 
                    'N1542A', 'N345AA', 'N567JB', 'N789DN', 'N890UA'],
        'CRSElapsedTime': [227, 227, 160, 183, 116, 355, 240, 190, 210, 280],
        'ActualElapsedTime': [230, 235, 170, 185, 110, 385, 280, 188, 235, 295],
        'Distance': [1400, 1416, 1089, 1576, 762, 2475, 2586, 733, 1372, 2400]
    }
    
    flights_df = pd.DataFrame(flights_data)
    flights_df.to_parquet(data_dir / 'flights.parquet', index=False)
    
    # 5. Create enhanced titanic.xlsx
    print("5. Creating enhanced titanic.xlsx...")
    
    titanic_data = {
        'PassengerId': list(range(1, 21)),
        'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 3, 2, 2, 3, 2, 1, 3, 2, 3, 1, 3, 2],
        'Name': [
            'Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley', 
            'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath', 
            'Allen, Mr. William Henry', 'Moran, Mr. James', 
            'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard', 
            'Johnson, Mrs. Oscar W', 'Nasser, Mrs. Nicholas',
            'Sandstrom, Miss. Marguerite Rut', 'Bonnell, Miss. Elizabeth',
            'Saundercock, Mr. William Henry', 'Andersson, Mr. Anders Johan',
            'Vestrom, Miss. Hulda Amanda Adolfina', 'Hewlett, Mrs. Mary D',
            'Rice, Master. Eugene', 'Williams, Mr. Charles Eugene',
            'Vander Planke, Mrs. Julius', 'Masselmani, Mrs. Fatima'
        ],
        'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 
               'male', 'male', 'female', 'female', 'female', 'female',
               'male', 'male', 'female', 'female', 'male', 'male',
               'female', 'female'],
        'Age': [22, 38, 26, 35, 35, np.nan, 54, 2, 27, 14, 
               24, 30, 45, 40, 25, 33, 4, 28, 31, np.nan],
        'SibSp': [1, 1, 0, 1, 0, 0, 0, 3, 0, 1, 0, 0, 0, 1, 0, 1, 4, 0, 0, 0],
        'Parch': [0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07,
                16.10, 8.05, 13.00, 31.28, 7.75, 16.00, 15.50, 13.50, 14.45, 7.23],
        'Cabin': [np.nan, 'C85', np.nan, 'C123', np.nan, np.nan, 'E46', np.nan, 
                 np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 
                 np.nan, np.nan, np.nan, np.nan],
        'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', 'C',
                    'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'C']
    }
    
    titanic_df = pd.DataFrame(titanic_data)
    titanic_df.to_excel(data_dir / 'titanic.xlsx', index=False)
    
    print("\n✓ All sample data files created successfully!")

# Create sample data files
create_sample_data()

# ============================================================================
# PART 2: MERGING AND JOINING
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: MERGING AND JOINING")
print("=" * 80)

# ----------------------------------------------------------------------------
# Task 1: Inner Join on Chinook Database
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 2.1: Inner Join on Chinook Database")
print("-" * 60)

try:
    # Load the database
    conn = sqlite3.connect(data_dir / 'chinook.db')
    
    # Load customers and invoices tables
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)
    
    print("Customers table (first 3 rows):")
    print(customers_df[['CustomerId', 'FirstName', 'LastName', 'Country']].head(3))
    print(f"\nCustomers shape: {customers_df.shape}")
    
    print("\nInvoices table (first 3 rows):")
    print(invoices_df[['InvoiceId', 'CustomerId', 'Total']].head(3))
    print(f"Invoices shape: {invoices_df.shape}")
    
    # Perform inner join
    customer_invoices = pd.merge(
        customers_df,
        invoices_df,
        on='CustomerId',
        how='inner'
    )
    
    print(f"\nAfter inner join - Shape: {customer_invoices.shape}")
    print("\nJoined data (first 3 rows):")
    print(customer_invoices[['CustomerId', 'FirstName', 'LastName', 'InvoiceId', 'Total']].head(3))
    
    # Find total number of invoices for each customer
    invoice_counts = customer_invoices.groupby(['CustomerId', 'FirstName', 'LastName']).agg(
        total_invoices=('InvoiceId', 'count'),
        total_spent=('Total', 'sum'),
        average_invoice=('Total', 'mean')
    ).reset_index()
    
    print("\n" + "=" * 40)
    print("TOTAL INVOICES PER CUSTOMER")
    print("=" * 40)
    
    for idx, row in invoice_counts.iterrows():
        print(f"\nCustomer: {row['FirstName']} {row['LastName']}")
        print(f"  Total Invoices: {row['total_invoices']}")
        print(f"  Total Spent: ${row['total_spent']:.2f}")
        print(f"  Average Invoice: ${row['average_invoice']:.2f}")
    
    # Customers with no invoices (would be shown with outer join)
    customers_without_invoices = customers_df[
        ~customers_df['CustomerId'].isin(invoices_df['CustomerId'])
    ]
    print(f"\nCustomers without invoices: {len(customers_without_invoices)}")
    
    conn.close()
    
except Exception as e:
    print(f"Error in Chinook join task: {e}")

# ----------------------------------------------------------------------------
# Task 2: Outer Join on Movie Data
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 2.2: Outer Join on Movie Data")
print("-" * 60)

try:
    # Load movie data
    movie_df = pd.read_csv(data_dir / 'movie.csv')
    
    print("Original Movie DataFrame shape:", movie_df.shape)
    print("\nColumns:", list(movie_df.columns))
    
    # Create two smaller DataFrames
    director_color_df = movie_df[['director_name', 'color']].copy()
    director_reviews_df = movie_df[['director_name', 'num_critic_for_reviews']].copy()
    
    # Remove duplicates for demonstration
    director_color_df = director_color_df.drop_duplicates()
    
    print(f"\nDataFrame 1 (director_name, color):")
    print(f"Shape: {director_color_df.shape}")
    print(director_color_df.head())
    
    print(f"\nDataFrame 2 (director_name, num_critic_for_reviews):")
    print(f"Shape: {director_reviews_df.shape}")
    print(director_reviews_df.head())
    
    # Perform left join
    left_join_df = pd.merge(
        director_color_df,
        director_reviews_df,
        on='director_name',
        how='left'
    )
    
    print(f"\nLEFT JOIN - Results:")
    print(f"Shape: {left_join_df.shape}")
    print(f"Number of rows: {len(left_join_df)}")
    print(left_join_df.head(10))
    
    # Perform full outer join
    outer_join_df = pd.merge(
        director_color_df,
        director_reviews_df,
        on='director_name',
        how='outer'
    )
    
    print(f"\nFULL OUTER JOIN - Results:")
    print(f"Shape: {outer_join_df.shape}")
    print(f"Number of rows: {len(outer_join_df)}")
    print(outer_join_df.head(10))
    
    # Analysis of join results
    print("\n" + "=" * 40)
    print("JOIN ANALYSIS")
    print("=" * 40)
    print(f"Unique directors in DataFrame 1: {director_color_df['director_name'].nunique()}")
    print(f"Unique directors in DataFrame 2: {director_reviews_df['director_name'].nunique()}")
    print(f"\nRows in left join: {len(left_join_df)}")
    print(f"Rows in full outer join: {len(outer_join_df)}")
    print(f"Difference (outer - left): {len(outer_join_df) - len(left_join_df)}")
    
    # Check for null values in joins
    print(f"\nNull values in left join: {left_join_df.isnull().sum().sum()}")
    print(f"Null values in outer join: {outer_join_df.isnull().sum().sum()}")
    
    # Which directors were added in outer join?
    directors_left = set(left_join_df['director_name'])
    directors_outer = set(outer_join_df['director_name'])
    added_directors = directors_outer - directors_left
    print(f"\nDirectors added in outer join: {added_directors}")
    
except Exception as e:
    print(f"Error in movie join task: {e}")

# ============================================================================
# PART 3: GROUPING AND AGGREGATING
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: GROUPING AND AGGREGATING")
print("=" * 80)

# ----------------------------------------------------------------------------
# Task 1: Grouped Aggregations on Titanic
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 3.1: Grouped Aggregations on Titanic")
print("-" * 60)

try:
    # Load titanic data
    titanic_df = pd.read_excel(data_dir / 'titanic.xlsx')
    
    print("Titanic Dataset Overview:")
    print(f"Total passengers: {len(titanic_df)}")
    print(f"Columns: {list(titanic_df.columns)}")
    
    # Group by Pclass and calculate aggregations
    titanic_grouped = titanic_df.groupby('Pclass').agg({
        'Age': ['mean', 'median', 'min', 'max'],
        'Fare': ['sum', 'mean', 'min', 'max'],
        'PassengerId': 'count',
        'Survived': ['mean', 'sum']
    }).round(2)
    
    # Rename columns for clarity
    titanic_grouped.columns = [
        'avg_age', 'median_age', 'min_age', 'max_age',
        'total_fare', 'avg_fare', 'min_fare', 'max_fare',
        'passenger_count',
        'survival_rate', 'survivors_count'
    ]
    
    print("\n" + "=" * 60)
    print("AGGREGATIONS BY PASSENGER CLASS")
    print("=" * 60)
    print(titanic_grouped.to_string())
    
    # Additional insights
    print("\n" + "=" * 40)
    print("KEY INSIGHTS")
    print("=" * 40)
    
    for pclass in titanic_grouped.index:
        print(f"\nPclass {pclass}:")
        print(f"  Passengers: {titanic_grouped.loc[pclass, 'passenger_count']}")
        print(f"  Average Age: {titanic_grouped.loc[pclass, 'avg_age']:.1f} years")
        print(f"  Total Fare Collected: ${titanic_grouped.loc[pclass, 'total_fare']:,.2f}")
        print(f"  Survival Rate: {titanic_grouped.loc[pclass, 'survival_rate']*100:.1f}%")
    
except Exception as e:
    print(f"Error in Titanic grouping task: {e}")

# ----------------------------------------------------------------------------
# Task 2: Multi-level Grouping on Movie Data
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 3.2: Multi-level Grouping on Movie Data")
print("-" * 60)

try:
    # Load movie data
    movie_df = pd.read_csv(data_dir / 'movie.csv')
    
    print("Movie Dataset Overview:")
    print(f"Total movies: {len(movie_df)}")
    print(f"Unique colors: {movie_df['color'].nunique()}")
    print(f"Unique directors: {movie_df['director_name'].nunique()}")
    
    # Multi-level grouping by color and director_name
    movie_grouped = movie_df.groupby(['color', 'director_name']).agg({
        'num_critic_for_reviews': ['sum', 'mean', 'count'],
        'duration': ['mean', 'min', 'max'],
        'imdb_score': ['mean', 'max']
    }).round(2)
    
    # Flatten column names
    movie_grouped.columns = [
        'total_reviews', 'avg_reviews', 'movie_count',
        'avg_duration', 'min_duration', 'max_duration',
        'avg_imdb_score', 'max_imdb_score'
    ]
    
    print("\n" + "=" * 60)
    print("MULTI-LEVEL GROUPING RESULTS")
    print("=" * 60)
    print(movie_grouped.to_string())
    
    # Top directors by reviews
    print("\n" + "=" * 40)
    print("TOP DIRECTORS BY REVIEWS")
    print("=" * 40)
    
    top_by_reviews = movie_grouped.nlargest(5, 'total_reviews')
    for (color, director), row in top_by_reviews.iterrows():
        print(f"\n{director} ({color}):")
        print(f"  Total Reviews: {row['total_reviews']}")
        print(f"  Movies: {row['movie_count']}")
        print(f"  Avg Duration: {row['avg_duration']} min")
    
    # Average duration by color
    print("\n" + "=" * 40)
    print("AVERAGE DURATION BY COLOR")
    print("=" * 40)
    
    duration_by_color = movie_df.groupby('color')['duration'].agg(['mean', 'min', 'max']).round(1)
    print(duration_by_color.to_string())
    
except Exception as e:
    print(f"Error in movie multi-level grouping task: {e}")

# ----------------------------------------------------------------------------
# Task 3: Nested Grouping on Flights
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 3.3: Nested Grouping on Flights")
print("-" * 60)

try:
    # Load flights data
    flights_df = pd.read_parquet(data_dir / 'flights.parquet')
    
    print("Flights Dataset Overview:")
    print(f"Total flights: {len(flights_df)}")
    print(f"Date range: {flights_df['Year'].min()}-{flights_df['Month'].min()} to "
          f"{flights_df['Year'].max()}-{flights_df['Month'].max()}")
    
    # Nested grouping by Year and Month
    flights_grouped = flights_df.groupby(['Year', 'Month']).agg({
        'FlightNum': 'count',
        'ArrDelay': ['mean', 'median', 'min', 'max'],
        'DepDelay': ['mean', 'max'],
        'Distance': ['mean', 'sum'],
        'Carrier': lambda x: x.nunique()
    }).round(2)
    
    # Flatten column names
    flights_grouped.columns = [
        'total_flights',
        'avg_arr_delay', 'median_arr_delay', 'min_arr_delay', 'max_arr_delay',
        'avg_dep_delay', 'max_dep_delay',
        'avg_distance', 'total_distance',
        'unique_carriers'
    ]
    
    print("\n" + "=" * 60)
    print("NESTED GROUPING BY YEAR AND MONTH")
    print("=" * 60)
    print(flights_grouped.to_string())
    
    # Monthly comparison
    print("\n" + "=" * 40)
    print("MONTHLY COMPARISON")
    print("=" * 40)
    
    for (year, month), row in flights_grouped.iterrows():
        print(f"\n{year}-{month:02d}:")
        print(f"  Flights: {row['total_flights']}")
        print(f"  Avg Departure Delay: {row['avg_dep_delay']:.1f} min")
        print(f"  Max Departure Delay: {row['max_dep_delay']} min")
        print(f"  Avg Arrival Delay: {row['avg_arr_delay']:.1f} min")
        print(f"  Total Distance: {row['total_distance']:,.0f} miles")
    
except Exception as e:
    print(f"Error in flights grouping task: {e}")

# ============================================================================
# PART 4: APPLYING FUNCTIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: APPLYING FUNCTIONS")
print("=" * 80)

# ----------------------------------------------------------------------------
# Task 1: Apply a Custom Function on Titanic
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 4.1: Apply Custom Function on Titanic")
print("-" * 60)

try:
    # Reload titanic data
    titanic_df = pd.read_excel(data_dir / 'titanic.xlsx')
    
    # Define function to classify age group
    def classify_age_group(age):
        """Classify passenger as Child (<18) or Adult (>=18)"""
        if pd.isna(age):
            return 'Unknown'
        elif age < 18:
            return 'Child'
        else:
            return 'Adult'
    
    # Apply the function to create new column
    titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age_group)
    
    print("Age Classification Results:")
    print(titanic_df[['Name', 'Age', 'Age_Group']].head(10))
    
    # Analyze age groups
    age_group_stats = titanic_df.groupby('Age_Group').agg({
        'PassengerId': 'count',
        'Survived': ['mean', 'sum'],
        'Age': ['mean', 'min', 'max'],
        'Fare': 'mean'
    }).round(2)
    
    age_group_stats.columns = [
        'count', 'survival_rate', 'survivors',
        'avg_age', 'min_age', 'max_age', 'avg_fare'
    ]
    
    print("\n" + "=" * 40)
    print("AGE GROUP ANALYSIS")
    print("=" * 40)
    print(age_group_stats.to_string())
    
    # Alternative: Using lambda function
    titanic_df['Age_Group_Lambda'] = titanic_df['Age'].apply(
        lambda x: 'Child' if not pd.isna(x) and x < 18 else ('Adult' if not pd.isna(x) else 'Unknown')
    )
    
    # Verify both methods produce same result
    print(f"\nBoth methods produce same results: "
          f"{titanic_df['Age_Group'].equals(titanic_df['Age_Group_Lambda'])}")
    
except Exception as e:
    print(f"Error in Titanic apply function task: {e}")

# ----------------------------------------------------------------------------
# Task 2: Normalize Employee Salaries
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 4.2: Normalize Employee Salaries")
print("-" * 60)

try:
    # Load employee data
    employee_df = pd.read_csv(data_dir / 'employee.csv')
    
    print("Original Employee Data:")
    print(employee_df)
    
    # Define normalization function
    def normalize_salary(group):
        """Normalize salaries within a department to 0-1 range"""
        min_sal = group['salary'].min()
        max_sal = group['salary'].max()
        if max_sal > min_sal:
            group['salary_normalized'] = (group['salary'] - min_sal) / (max_sal - min_sal)
        else:
            group['salary_normalized'] = 0.5  # All salaries equal
        return group
    
    # Apply normalization by department
    employee_normalized = employee_df.groupby('department').apply(normalize_salary)
    employee_normalized = employee_normalized.reset_index(drop=True)
    
    # Alternative: Using transform
    employee_df['salary_normalized_transform'] = employee_df.groupby('department')['salary'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() > x.min() else 0.5
    )
    
    print("\n" + "=" * 60)
    print("EMPLOYEE SALARIES NORMALIZED BY DEPARTMENT")
    print("=" * 60)
    
    for dept in employee_normalized['department'].unique():
        dept_data = employee_normalized[employee_normalized['department'] == dept]
        print(f"\n{dept} Department:")
        print(f"  Salary Range: ${dept_data['salary'].min():,.0f} - ${dept_data['salary'].max():,.0f}")
        print("  Normalized Salaries:")
        for _, row in dept_data.iterrows():
            print(f"    {row['name']}: ${row['salary']:,.0f} -> {row['salary_normalized']:.3f}")
    
    # Calculate department statistics
    dept_stats = employee_df.groupby('department').agg({
        'salary': ['mean', 'min', 'max', 'std'],
        'employee_id': 'count'
    }).round(2)
    
    dept_stats.columns = ['avg_salary', 'min_salary', 'max_salary', 'std_salary', 'employee_count']
    
    print("\n" + "=" * 40)
    print("DEPARTMENT SALARY STATISTICS")
    print("=" * 40)
    print(dept_stats.to_string())
    
    # Z-score normalization alternative
    employee_df['salary_zscore'] = employee_df.groupby('department')['salary'].transform(
        lambda x: (x - x.mean()) / x.std() if x.std() > 0 else 0
    )
    
    print("\nZ-Score Normalization (first 5 rows):")
    print(employee_df[['name', 'department', 'salary', 'salary_zscore']].head())
    
except Exception as e:
    print(f"Error in employee salary normalization task: {e}")

# ----------------------------------------------------------------------------
# Task 3: Custom Function on Movies
# ----------------------------------------------------------------------------
print("\n" + "-" * 60)
print("Task 4")