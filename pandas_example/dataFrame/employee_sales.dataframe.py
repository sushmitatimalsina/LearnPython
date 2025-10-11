import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['Sita', 'Gita', 'Hari', 'Rita', 'Nabin', None],
    'department': ['IT', 'HR', 'Finance', None, 'IT', 'Finance'],
    'city': ['Kathmandu', 'Pokhara', 'Lalitpur', 'Biratnagar', None, 'Pokhara']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 7],
    'basic_salary': [50000, 60000, 55000, None, 58000, 45000],
    'bonus': [5000, 4000, None, 3000, 2000, 1000],
    'month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan']
})

employees['name'].fillna('Unknown', inplace=True)
employees['department'].fillna('Unknown', inplace=True)
employees['city'].fillna('Unknown', inplace=True)

salaries['basic_salary'].fillna(0, inplace=True)
salaries['bonus'].fillna(0, inplace=True)

print(" employees:")
print(employees)

print("salaries")
print(salaries)

merged_df = pd.merge(employees, salaries, on='emp_id', how='left')
print(merged_df)

merged_df['total_salary'] = merged_df['basic_salary'] + merged_df['bonus']
print(merged_df)