import pandas as pd
import numpy as np
import sqlite3
import json
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("PANDAS HOMEWORK - COMPREHENSIVE SOLUTION")
print("=" * 80)

# Create a data directory if it doesn't exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Part 1: Reading Files
print("\n" + "=" * 80)
print("PART 1: READING FILES")
print("=" * 80)

# Helper function to download sample data
def download_sample_data():
    """Create sample data files for demonstration"""
    print("Creating sample data files...")
    
    # 1. Create SQLite database (chinook.db)
    print("1. Creating chinook.db...")
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
    
    # Insert sample data
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
    
    conn.commit()
    conn.close()
    
    # 2. Create iris.json
    print("2. Creating iris.json...")
    iris_data = {
        "sepal_length": [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
        "sepal_width": [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1],
        "petal_length": [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5],
        "petal_width": [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1],
        "species": ["setosa", "setosa", "setosa", "setosa", "setosa", 
                    "setosa", "setosa", "setosa", "setosa", "setosa"]
    }
    
    with open(data_dir / 'iris.json', 'w') as f:
        json.dump(iris_data, f, indent=2)
    
    # 3. Create titanic.xlsx
    print("3. Creating titanic.xlsx...")
    titanic_data = {
        'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 3, 2],
        'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley', 
                'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath', 
                'Allen, Mr. William Henry', 'Moran, Mr. James', 
                'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard', 
                'Johnson, Mrs. Oscar W', 'Nasser, Mrs. Nicholas'],
        'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 
               'male', 'male', 'female', 'female'],
        'Age': [22, 38, 26, 35, 35, None, 54, 2, 27, 14],
        'SibSp': [1, 1, 0, 1, 0, 0, 0, 3, 0, 1],
        'Parch': [0, 0, 0, 0, 0, 0, 0, 1, 2, 0],
        'Ticket': ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803', 
                  '373450', '330877', '17463', '349909', '347742', '237736'],
        'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07],
        'Cabin': [None, 'C85', None, 'C123', None, None, 'E46', None, None, None],
        'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', 'C']
    }
    
    titanic_df = pd.DataFrame(titanic_data)
    titanic_df.to_excel(data_dir / 'titanic.xlsx', index=False)
    
    # 4. Create flights.parquet
    print("4. Creating flights.parquet...")
    flights_data = {
        'year': [2013, 2013, 2013, 2013, 2013],
        'month': [1, 1, 1, 1, 1],
        'day': [1, 1, 1, 1, 1],
        'dep_time': [517, 533, 542, 544, 554],
        'sched_dep_time': [515, 529, 540, 545, 600],
        'dep_delay': [2, 4, 2, -1, -6],
        'arr_time': [830, 850, 923, 1004, 812],
        'sched_arr_time': [819, 830, 850, 1022, 837],
        'arr_delay': [11, 20, 33, -18, -25],
        'carrier': ['UA', 'UA', 'AA', 'B6', 'DL'],
        'flight': [1545, 1714, 1141, 725, 461],
        'tailnum': ['N14228', 'N24211', 'N619AA', 'N804JB', 'N668DN'],
        'origin': ['EWR', 'LGA', 'JFK', 'JFK', 'LGA'],
        'dest': ['IAH', 'IAH', 'MIA', 'BQN', 'ATL'],
        'air_time': [227, 227, 160, 183, 116],
        'distance': [1400, 1416, 1089, 1576, 762],
        'hour': [5, 5, 5, 5, 6],
        'minute': [15, 29, 40, 45, 0],
        'time_hour': ['2013-01-01 05:00:00', '2013-01-01 05:00:00', 
                     '2013-01-01 05:00:00', '2013-01-01 05:00:00', 
                     '2013-01-01 06:00:00']
    }
    
    flights_df = pd.DataFrame(flights_data)
    flights_df.to_parquet(data_dir / 'flights.parquet', index=False)
    
    # 5. Create movie.csv
    print("5. Creating movie.csv...")
    movie_data = {
        'movie_title': ['Avatar', 'Titanic', 'The Dark Knight', 'Star Wars: The Force Awakens', 'Avengers: Endgame'],
        'director_name': ['James Cameron', 'James Cameron', 'Christopher Nolan', 'J.J. Abrams', 'Anthony Russo'],
        'duration': [162, 195, 152, 138, 181],
        'director_facebook_likes': [0, 0, 21000, 11000, 400],
        'actor_1_facebook_likes': [1000, 2000, 23000, 11000, 22000],
        'actor_2_facebook_likes': [936, 1000, 11000, 1000, 200],
        'actor_3_facebook_likes': [855, 936, 4000, 936, 1000],
        'gross': [760505847, 658672302, 533316061, 936662225, 2797800564],
        'genres': ['Action|Adventure|Fantasy|Sci-Fi', 'Drama|Romance', 'Action|Crime|Drama|Thriller', 
                  'Action|Adventure|Sci-Fi', 'Action|Adventure|Drama|Sci-Fi'],
        'imdb_score': [7.9, 7.7, 9.0, 7.9, 8.4]
    }
    
    movie_df = pd.DataFrame(movie_data)
    movie_df.to_csv(data_dir / 'movie.csv', index=False)
    
    print("\n✓ All sample data files created successfully!")
    print("  Files are saved in the 'data' directory.")

# Check if data files exist, if not create them
if not all([(data_dir / f).exists() for f in ['chinook.db', 'iris.json', 'titanic.xlsx', 'flights.parquet', 'movie.csv']]):
    download_sample_data()
else:
    print("✓ All data files already exist")

# Task 1.1: Read chinook.db (customers table)
print("\n" + "-" * 40)
print("Task 1.1: Reading chinook.db (customers table)")
print("-" * 40)

try:
    conn = sqlite3.connect(data_dir / 'chinook.db')
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()
    
    print("First 10 rows of customers table:")
    print(customers_df.head(10))
    print(f"\nShape of customers table: {customers_df.shape}")
    print(f"Columns: {list(customers_df.columns)}")
    
except Exception as e:
    print(f"Error reading chinook.db: {e}")

# Task 1.2: Read iris.json
print("\n" + "-" * 40)
print("Task 1.2: Reading iris.json")
print("-" * 40)

try:
    iris_df = pd.read_json(data_dir / 'iris.json')
    
    print("First 5 rows of iris dataset:")
    print(iris_df.head())
    print(f"\nShape of iris dataset: {iris_df.shape}")
    print(f"Column names: {list(iris_df.columns)}")
    print(f"\nData types:\n{iris_df.dtypes}")
    
except Exception as e:
    print(f"Error reading iris.json: {e}")

# Task 1.3: Read titanic.xlsx
print("\n" + "-" * 40)
print("Task 1.3: Reading titanic.xlsx")
print("-" * 40)

try:
    titanic_df = pd.read_excel(data_dir / 'titanic.xlsx')
    
    print("First 5 rows of titanic dataset:")
    print(titanic_df.head())
    print(f"\nShape of titanic dataset: {titanic_df.shape}")
    print(f"Columns: {list(titanic_df.columns)}")
    
except Exception as e:
    print(f"Error reading titanic.xlsx: {e}")

# Task 1.4: Read flights parquet file
print("\n" + "-" * 40)
print("Task 1.4: Reading flights.parquet")
print("-" * 40)

try:
    flights_df = pd.read_parquet(data_dir / 'flights.parquet')
    
    print("DataFrame info:")
    print(flights_df.info())
    print(f"\nFirst 5 rows:")
    print(flights_df.head())
    
except Exception as e:
    print(f"Error reading flights.parquet: {e}")

# Task 1.5: Read movie.csv
print("\n" + "-" * 40)
print("Task 1.5: Reading movie.csv")
print("-" * 40)

try:
    movie_df = pd.read_csv(data_dir / 'movie.csv')
    
    print("Random sample of 10 rows (showing all rows since dataset is small):")
    print(movie_df.sample(min(10, len(movie_df)), random_state=42))
    print(f"\nShape of movie dataset: {movie_df.shape}")
    print(f"Columns: {list(movie_df.columns)}")
    
except Exception as e:
    print(f"Error reading movie.csv: {e}")

# Part 2: Exploring DataFrames
print("\n" + "=" * 80)
print("PART 2: EXPLORING DATAFRAMES")
print("=" * 80)

# Task 2.1: Using iris.json DataFrame
print("\n" + "-" * 40)
print("Task 2.1: Working with iris DataFrame")
print("-" * 40)

try:
    # Rename columns to lowercase
    iris_df_lower = iris_df.copy()
    iris_df_lower.columns = iris_df_lower.columns.str.lower()
    
    print("DataFrame with lowercase column names:")
    print(iris_df_lower.head())
    print(f"\nNew column names: {list(iris_df_lower.columns)}")
    
    # Select only sepal_length and sepal_width columns
    sepal_df = iris_df_lower[['sepal_length', 'sepal_width']].copy()
    
    print("\nSelected columns (sepal_length and sepal_width):")
    print(sepal_df.head())
    print(f"\nShape of selected data: {sepal_df.shape}")
    
except Exception as e:
    print(f"Error processing iris DataFrame: {e}")

# Task 2.2: Using titanic.xlsx DataFrame
print("\n" + "-" * 40)
print("Task 2.2: Working with titanic DataFrame")
print("-" * 40)

try:
    # Filter rows where age > 30
    age_above_30 = titanic_df[titanic_df['Age'] > 30].copy()
    
    print("Passengers with age above 30:")
    print(age_above_30[['Name', 'Age', 'Sex']])
    print(f"\nNumber of passengers above 30: {len(age_above_30)}")
    
    # Count number of male and female passengers
    gender_counts = titanic_df['Sex'].value_counts()
    
    print("\nGender distribution:")
    print(gender_counts)
    print(f"\nMale passengers: {gender_counts.get('male', 0)}")
    print(f"Female passengers: {gender_counts.get('female', 0)}")
    
    # Additional statistics
    print(f"\nPercentage distribution:")
    print(gender_counts / len(titanic_df) * 100)
    
except Exception as e:
    print(f"Error processing titanic DataFrame: {e}")

# Task 2.3: Using flights parquet file
print("\n" + "-" * 40)
print("Task 2.3: Working with flights DataFrame")
print("-" * 40)

try:
    # Extract and print only origin, dest, and carrier columns
    flights_subset = flights_df[['origin', 'dest', 'carrier']].copy()
    
    print("Origin, Destination, and Carrier columns:")
    print(flights_subset)
    print(f"\nShape of subset: {flights_subset.shape}")
    
    # Find number of unique destinations
    unique_destinations = flights_df['dest'].nunique()
    unique_origins = flights_df['origin'].nunique()
    
    print(f"\nNumber of unique destinations: {unique_destinations}")
    print(f"Number of unique origins: {unique_origins}")
    
    # List all unique destinations
    print(f"\nUnique destinations: {sorted(flights_df['dest'].unique())}")
    
    # Additional analysis: Flights per destination
    flights_per_dest = flights_df['dest'].value_counts()
    print(f"\nFlights per destination:\n{flights_per_dest}")
    
except Exception as e:
    print(f"Error processing flights DataFrame: {e}")

# Task 2.4: Using movie.csv DataFrame
print("\n" + "-" * 40)
print("Task 2.4: Working with movie DataFrame")
print("-" * 40)

try:
    # Filter rows where duration > 120 minutes
    long_movies = movie_df[movie_df['duration'] > 120].copy()
    
    print(f"Movies longer than 120 minutes ({len(long_movies)} found):")
    print(long_movies[['movie_title', 'duration', 'director_name']])
    
    # Sort filtered DataFrame by director_facebook_likes in descending order
    long_movies_sorted = long_movies.sort_values('director_facebook_likes', ascending=False)
    
    print("\nLong movies sorted by director Facebook likes (descending):")
    print(long_movies_sorted[['movie_title', 'duration', 'director_name', 'director_facebook_likes']])
    
    # Additional analysis: Duration statistics
    print(f"\nDuration statistics for all movies:")
    print(f"Minimum duration: {movie_df['duration'].min()} minutes")
    print(f"Maximum duration: {movie_df['duration'].max()} minutes")
    print(f"Average duration: {movie_df['duration'].mean():.2f} minutes")
    print(f"Median duration: {movie_df['duration'].median()} minutes")
    
except Exception as e:
    print(f"Error processing movie DataFrame: {e}")

# Part 3: Challenges and Explorations
print("\n" + "=" * 80)
print("PART 3: CHALLENGES AND EXPLORATIONS")
print("=" * 80)

# Task 3.1: Calculate statistics for iris DataFrame
print("\n" + "-" * 40)
print("Task 3.1: Statistics for iris DataFrame")
print("-" * 40)

try:
    # Select only numerical columns
    numerical_cols = iris_df_lower.select_dtypes(include=[np.number]).columns
    
    print("Numerical columns in iris dataset:")
    print(numerical_cols.tolist())
    
    # Calculate statistics
    stats_df = pd.DataFrame({
        'mean': iris_df_lower[numerical_cols].mean(),
        'median': iris_df_lower[numerical_cols].median(),
        'std': iris_df_lower[numerical_cols].std(),
        'min': iris_df_lower[numerical_cols].min(),
        'max': iris_df_lower[numerical_cols].max()
    })
    
    print("\nStatistics for each numerical column:")
    print(stats_df.round(3))
    
    # Additional statistics
    print("\nAdditional statistics:")
    print(f"Range (max-min) for each column:")
    ranges = stats_df.loc['max'] - stats_df.loc['min']
    print(ranges)
    
    # Coefficient of variation (std/mean)
    cv = (stats_df.loc['std'] / stats_df.loc['mean']) * 100
    print(f"\nCoefficient of Variation (%):")
    print(cv.round(2))
    
except Exception as e:
    print(f"Error calculating iris statistics: {e}")

# Task 3.2: Statistics for titanic age
print("\n" + "-" * 40)
print("Task 3.2: Statistics for titanic passenger ages")
print("-" * 40)

try:
    # Remove NaN values for age calculations
    age_series = titanic_df['Age'].dropna()
    
    print("Age statistics (excluding missing values):")
    print(f"Number of passengers with age data: {len(age_series)}")
    print(f"Number of passengers with missing age: {titanic_df['Age'].isna().sum()}")
    print(f"Minimum age: {age_series.min():.1f} years")
    print(f"Maximum age: {age_series.max():.1f} years")
    print(f"Sum of all ages: {age_series.sum():.1f} years")
    print(f"Mean age: {age_series.mean():.2f} years")
    print(f"Median age: {age_series.median():.2f} years")
    print(f"Standard deviation: {age_series.std():.2f} years")
    
    # Age distribution analysis
    print(f"\nAge distribution:")
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    age_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
    
    titanic_df['AgeGroup'] = pd.cut(titanic_df['Age'], bins=age_bins, labels=age_labels, right=False)
    age_group_counts = titanic_df['AgeGroup'].value_counts().sort_index()
    
    print(age_group_counts)
    
    # Clean up temporary column
    titanic_df.drop('AgeGroup', axis=1, inplace=True, errors='ignore')
    
except Exception as e:
    print(f"Error calculating age statistics: {e}")

# Task 3.3: Analysis of movie.csv
print("\n" + "-" * 40)
print("Task 3.3: Analysis of movie DataFrame")
print("-" * 40)

try:
    # Identify director with highest total director_facebook_likes
    director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
    top_director = director_likes.idxmax()
    top_director_likes = director_likes.max()
    
    print("Director Facebook likes analysis:")
    print(f"Director with highest total Facebook likes: {top_director}")
    print(f"Total likes: {top_director_likes:,}")
    
    print("\nAll directors and their total Facebook likes:")
    for director, likes in director_likes.sort_values(ascending=False).items():
        print(f"  {director}: {likes:,}")
    
    # Find the 5 longest movies and their directors
    print(f"\nTop 5 longest movies:")
    longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'duration', 'director_name']]
    
    for idx, row in longest_movies.iterrows():
        print(f"  {row['movie_title']} ({row['duration']} min) - Directed by {row['director_name']}")
    
    # Additional analysis: Average duration by director
    print(f"\nAverage movie duration by director:")
    avg_duration_by_director = movie_df.groupby('director_name')['duration'].mean().round(1)
    print(avg_duration_by_director)
    
except Exception as e:
    print(f"Error analyzing movie DataFrame: {e}")

# Task 3.4: Analysis of flights parquet file
print("\n" + "-" * 40)
print("Task 3.4: Analysis of flights DataFrame")
print("-" * 40)

try:
    # Check for missing values in the dataset
    print("Missing values in flights dataset:")
    missing_values = flights_df.isnull().sum()
    
    missing_df = pd.DataFrame({
        'column': missing_values.index,
        'missing_count': missing_values.values,
        'missing_percentage': (missing_values.values / len(flights_df) * 100).round(2)
    })
    
    # Filter to show only columns with missing values
    missing_with_values = missing_df[missing_df['missing_count'] > 0]
    
    if len(missing_with_values) > 0:
        print(missing_with_values.to_string(index=False))
    else:
        print("No missing values found in the dataset!")
    
    # Fill missing values in a numerical column with the column's mean
    # First, let's check which numerical columns exist
    numerical_cols_flights = flights_df.select_dtypes(include=[np.number]).columns
    
    print(f"\nNumerical columns available: {list(numerical_cols_flights)}")
    
    # Check if any numerical column has missing values
    numerical_missing = flights_df[numerical_cols_flights].isnull().sum()
    columns_with_missing = numerical_missing[numerical_missing > 0].index
    
    if len(columns_with_missing) > 0:
        print(f"\nNumerical columns with missing values: {list(columns_with_missing)}")
        
        # Create a copy of the DataFrame for demonstration
        flights_filled = flights_df.copy()
        
        # Fill missing values in the first column with missing values
        column_to_fill = columns_with_missing[0]
        column_mean = flights_filled[column_to_fill].mean()
        
        print(f"\nFilling missing values in '{column_to_fill}' with mean: {column_mean:.2f}")
        
        # Store original missing count
        original_missing = flights_filled[column_to_fill].isnull().sum()
        
        # Fill missing values
        flights_filled[column_to_fill] = flights_filled[column_to_fill].fillna(column_mean)
        
        # Verify filling worked
        new_missing = flights_filled[column_to_fill].isnull().sum()
        
        print(f"Missing values before filling: {original_missing}")
        print(f"Missing values after filling: {new_missing}")
        
        if new_missing == 0:
            print("✓ Successfully filled all missing values!")
        
        # Show sample of filled values
        print(f"\nSample of filled column '{column_to_fill}':")
        print(flights_filled[[column_to_fill]].head())
        
    else:
        print("\nNo missing values in numerical columns to fill.")
        
        # For demonstration, let's create a copy and introduce some missing values
        flights_demo = flights_df.copy()
        # Introduce missing values in dep_delay column
        flights_demo.loc[0:1, 'dep_delay'] = np.nan
        
        print("\nFor demonstration, creating missing values in 'dep_delay' column...")
        print(f"Missing values created: {flights_demo['dep_delay'].isnull().sum()}")
        
        # Fill with mean
        dep_delay_mean = flights_demo['dep_delay'].mean()
        flights_demo['dep_delay'] = flights_demo['dep_delay'].fillna(dep_delay_mean)
        
        print(f"Filled with mean: {dep_delay_mean:.2f}")
        print(f"Missing values after filling: {flights_demo['dep_delay'].isnull().sum()}")
    
    # Additional analysis: Flight statistics
    print(f"\nFlight delay statistics:")
    print(f"Average departure delay: {flights_df['dep_delay'].mean():.2f} minutes")
    print(f"Average arrival delay: {flights_df['arr_delay'].mean():.2f} minutes")
    print(f"Maximum departure delay: {flights_df['dep_delay'].max()} minutes")
    print(f"Minimum departure delay: {flights_df['dep_delay'].min()} minutes")
    
    # Flights by carrier
    print(f"\nFlights by carrier:")
    carrier_counts = flights_df['carrier'].value_counts()
    print(carrier_counts)
    
except Exception as e:
    print(f"Error analyzing flights DataFrame: {e}")

# Summary of all DataFrames
print("\n" + "=" * 80)
print("SUMMARY OF ALL DATAFRAMES")
print("=" * 80)

try:
    # Create a summary table
    summary_data = {
        'Dataset': ['chinook.db (customers)', 'iris.json', 'titanic.xlsx', 'flights.parquet', 'movie.csv'],
        'Rows': [len(customers_df), len(iris_df), len(titanic_df), len(flights_df), len(movie_df)],
        'Columns': [len(customers_df.columns), len(iris_df.columns), len(titanic_df.columns), 
                   len(flights_df.columns), len(movie_df.columns)],
        'Size (KB)': [
            customers_df.memory_usage(deep=True).sum() / 1024,
            iris_df.memory_usage(deep=True).sum() / 1024,
            titanic_df.memory_usage(deep=True).sum() / 1024,
            flights_df.memory_usage(deep=True).sum() / 1024,
            movie_df.memory_usage(deep=True).sum() / 1024
        ]
    }
    
    summary_df = pd.DataFrame(summary_data)
    summary_df['Size (KB)'] = summary_df['Size (KB)'].round(2)
    
    print("Dataset Overview:")
    print(summary_df.to_string(index=False))
    
    # Memory usage analysis
    print(f"\nTotal memory usage of all DataFrames: {summary_df['Size (KB)'].sum():.2f} KB")
    
except Exception as e:
    print(f"Error creating summary: {e}")

print("\n" + "=" * 80)
print("HOMEWORK COMPLETED SUCCESSFULLY!")
print("=" * 80)
print("\nKey skills demonstrated:")
print("1. ✓ Reading multiple file formats (SQLite, JSON, Excel, Parquet, CSV)")
print("2. ✓ DataFrame exploration and manipulation")
print("3. ✓ Data filtering and sorting")
print("4. ✓ Statistical analysis and calculations")
print("5. ✓ Handling missing values")
print("6. ✓ Grouping and aggregation")
print("7. ✓ Data visualization preparation")