import csv
from faker import Faker

fake = Faker()

# Define the number of rows to generate
num_rows = 100000

# Generate synthetic data for the Company table
companies = [{'Company_ID': i + 1, 'Company_Name': fake.company()} for i in range(num_rows)]

# Generate synthetic data for the Product table
products = [{'Product_ID': i + 1, 'Product_Name': fake.word()} for i in range(num_rows)]

# Generate synthetic data for the Terminal table
terminals = [{'Terminal_ID': i + 1, 'Terminal_Name': fake.company_suffix()} for i in range(num_rows)]

# Generate synthetic data for the StorageTank table
storage_tanks = [{'Tank_ID': i + 1, 'Tank_Number': fake.random_number(digits=4), 'Capacity': round(fake.random_number(digits=5) + 100, 2), 'Product_ID': i + 1, 'Terminal_ID': i + 1} for i in range(num_rows)]

# Generate synthetic data for the Order table
orders = [{'Order_ID': i + 1, 'Company_ID': i + 1, 'Product_ID': i + 1, 'Quantity': fake.random_number(digits=3), 'Order_Date': fake.date_time_this_year()} for i in range(num_rows)]

# Write data to CSV files
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_to_csv(companies, 'companies.csv')
write_to_csv(products, 'products.csv')
write_to_csv(terminals, 'terminals.csv')
write_to_csv(storage_tanks, 'storage_tanks.csv')
write_to_csv(orders, 'orders.csv')

print("Synthetic data generated and written to CSV files successfully.")
