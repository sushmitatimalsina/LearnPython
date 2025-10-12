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

df['email_domain'] = df['email'].str.split('@').str[1]
print("\n Email Domain:\n", df['email_domain'])

df['name_length'] = df['name'].str.len()
print("\n Name Length:\n", df['name_length'])

df['name_upper'] = df['name'].str.upper()
print(df['name_upper'])

gmail = df['email'].str.contains('gmail')
print(gmail)