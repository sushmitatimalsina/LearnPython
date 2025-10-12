import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4],
    'name': ['Sita Sharma', 'Gita Thapa', 'Hari KC', 'Rita Gurung'],
    'email': ['sita@gmail.com', 'gita@company.com', 'hari@gmail.com', 'rita@hotmail.com'],
    'department': ['IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df['first_name'] = df['name'].str.split().str[1]
print("\nFirst Names:\n", df['first_name'])


