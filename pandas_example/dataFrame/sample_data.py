import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', None],
    'department_id': [101, 102, 101, 103, None, 102],
    'salary': [70000, 54000, None, 90000, 60000, 50000],
    'join_date': ['2021-05-10', '2020-03-12', '2019-11-03', '2022-01-15', '2021-06-25', '2023-07-19']
})

departments = pd.DataFrame({
    'department_id': [101, 102, 103],
    'department_name': ['IT', 'HR', 'Finance'],
    'location': ['Kathmandu', 'Pokhara', 'Lalitpur']
})

# Handle missing values
employees['name'].fillna('Unknown', inplace=True)
employees['department_id'].fillna(0, inplace=True)
employees['salary'].fillna(employees['salary'].mean(), inplace=True)

# Convert join_date to datetime
employees['join_date'] = pd.to_datetime(employees['join_date'])

# Remove duplicates if any
employees.drop_duplicates(inplace=True)

merged_df = pd.merge(employees, departments, on='department_id', how='left')
print(merged_df)