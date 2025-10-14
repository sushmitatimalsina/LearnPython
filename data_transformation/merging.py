import pandas as pd

# Employee info
df1 = pd.DataFrame({
    'Employee_ID': [1, 2, 3],
    'Name': ['Aarav', 'Bina', 'Chirag']
})

# Employee salary
df2 = pd.DataFrame({
    'Employee_ID': [1, 2, 3],
    'Salary': [50000, 60000, 55000]
})

# Merge on Employee_ID
merged_df = pd.merge(df1, df2, on='Employee_ID')
print(merged_df)