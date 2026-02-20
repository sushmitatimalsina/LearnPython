import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# Step 0: Generate sample data
# -----------------------------

# Sample sales data
sales_data = pd.DataFrame({
    'sale_id': [1, 2, 3, 4],
    'customer_id': [101, 102, 103, 101],
    'product': ['Apple', 'Banana', 'Orange', 'Apple'],
    'quantity': [5, 3, 4, 2],
    'sale_date': ['2026-02-20', '2026-02-20', '2026-02-19', '2026-02-20']
})

# Sample customer data
customer_data = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'name': ['Sushmita', 'Raj', 'Anita'],
    'city': ['Kathmandu', 'Pokhara', 'Biratnagar']
})

# Optional: Save as CSV if you want to test reading from CSV
# sales_data.to_csv('daily_sales.csv', index=False)
# customer_data.to_csv('customers.csv', index=False)

# -----------------------------
# Step 1: Transform - Clean and merge data
# -----------------------------

# Remove duplicates
sales_data = sales_data.drop_duplicates()
customer_data = customer_data.drop_duplicates()

# Merge sales with customer info
merged_data = pd.merge(sales_data, customer_data, on='customer_id', how='left')

# Convert sale_date to datetime
merged_data['sale_date'] = pd.to_datetime(merged_data['sale_date'])

# -----------------------------
# Step 2: Load - Save to database
# -----------------------------

# Using SQLite for simplicity (no installation needed)
engine = create_engine('sqlite:///sales_db.sqlite')  # Creates a local SQLite file

merged_data.to_sql('cleaned_sales', engine, if_exists='replace', index=False)

print("ETL pipeline executed successfully!")
print("\nSample of merged data:")
print(merged_data)