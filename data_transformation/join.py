import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Aarav', 'Bina', 'Chirag'],
    'Department': ['IT', 'HR', 'Finance']
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    'Salary': [50000, 60000, 55000]
}, index=[1, 2, 3])

# Join df2 to df1
joined_df = df1.join(df2)
print(joined_df)