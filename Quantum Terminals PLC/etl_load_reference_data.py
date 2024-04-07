import glob
import pandas as pd
from sqlalchemy import create_engine

# Define PostgreSQL database connection
DB_URI = 'postgresql://trestle:password123@localhost:5432/quantumterminaldb'
engine = create_engine(DB_URI)

# Define a function to extract data from CSV files
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error extracting data from file {file_path}: {e}")
        return None

# Define a function to transform data
def transform_data(data):
    try:
        transformed_data = data.apply(lambda x: x.strip() if isinstance(x, str) else x)
        return transformed_data
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None


# Define a function to load data into PostgreSQL
def load_data(data, table_name):
    try:
        data.to_sql(table_name, engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Error loading data into table {table_name}: {e}")

# Define the file paths for the CSV files
csv_file_paths = [
    'quantum-db/companies.csv',
    'quantum-db/orders.csv',
    'quantum-db/products.csv',
    'quantum-db/storage_tanks.csv',
    'quantum-db/terminals.csv'
]

# Loop through the CSV files and extract, transform, and load the data
for file_path in csv_file_paths:
    print(f"Processing file {file_path}...")
    data = extract_data(file_path)
    if data is not None:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            table_name = file_path.split("/")[-1].split(".")[0]
            load_data(transformed_data, table_name)

print("All data inserted successfully into PostgreSQL database.")
