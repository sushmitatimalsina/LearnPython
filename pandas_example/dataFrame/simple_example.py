import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Sita', 'Gita', None, 'Rita', 'Hari'],
    'department': ['IT', None, 'Finance', 'HR', 'IT'],
    'salary': [50000, 60000, 55000, None, 58000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

missing_count = df.isnull().sum()
print("\nMissing Values Count:\n", missing_count)

