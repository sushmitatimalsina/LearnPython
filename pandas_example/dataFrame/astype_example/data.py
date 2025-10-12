import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4],
    'name': ['Sita', 'Gita', 'Hari', 'Rita'],
    'salary': ['50000', '60000', '55000', '58000'],  # as strings
    'bonus': ['5000', '4000', '3000', '4500'],       # as strings
    'joining_date': ['2024-01-10', '2024-02-15', '2024-03-20', '2024-04-25'],  # as strings
    'department_code': [101, 102, 103, 104]  # numeric code
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df.dtypes)

df['salary'] = df['salary'].astype(int)
df['bonus'] = df['bonus'].astype(int)
df['department_code'] = df['department_code'].astype(str)

df['joining_date'] = pd.to_datetime(df['joining_date'])
print("\nDataFrame after multiple type conversions:\n", df.dtypes)