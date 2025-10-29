import pandas as pd
import numpy as np

data = {
    'Name': [' Alice ', 'Bob', 'Charlie', 'David', 'Eve', 'Alice '],
    'Age': [25, np.nan, 30, 22, 29, 25],
    'City': ['New York', 'los angeles ', 'NEW YORK', np.nan, 'Chicago', 'New York'],
    'Salary': ['50000', '60000', '55000', 'not available', '58000', '50000'],
    'JoinDate': ['2021-01-05', '2020/05/12', '2021-13-10', '2022-07-15', '2021-08-10', '2021-01-05']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

print("\nData Info:")
print(df.info())

print("\nCheck for missing values:")
print(df.isnull().sum())

# Clean the data
df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.strip().str.title()

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)

# Convert JoinDate to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nCleaned DataFrame:\n", df)
