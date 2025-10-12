import pandas as pd

data = {
    'employee_id': [101, 102, 103, 104],
    'name': ['Sita', 'Gita', 'Hari', 'Rita'],
    'department': ['IT', 'HR', 'Finance', 'IT'],
    'salary': [50000, 60000, 55000, 58000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df.set_index('employee_id', inplace=True)
print("\nDataFrame after setting index:\n", df)

print("\nSelect employee with ID 103:\n", df.loc[103])
print("\nSelect employees 101 and 104:\n", df.loc[[101, 104]])

df_reset = df.reset_index()
print("\nDataFrame after resetting index:\n", df_reset)
