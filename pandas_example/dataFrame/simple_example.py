import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Sita', 'Gita', None, 'Rita', 'Hari'],
    'department': ['IT', None, 'Finance', 'HR', 'IT'],
    'salary': [50000, 60000, 55000, None, 58000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
missing_values = df.isnull()
print("\nMissing Values:\n", missing_values)

missing_count = df.isnull().sum()
print("\nMissing Values Count:\n", missing_count)

df_drop_rows = df.dropna()
print("\nDrop rows with missing values:\n", df_drop_rows)

df_drop_cols = df.dropna(axis=1)
print("\nDrop columns with missing values:\n", df_drop_cols)

df['name'].fillna('Unknown', inplace=True)
df['department'].fillna('General', inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
print("\nDataFrame after fillna():\n", df)