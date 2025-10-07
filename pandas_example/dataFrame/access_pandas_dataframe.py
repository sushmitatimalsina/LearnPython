import pandas as pd

data = {
        'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]
        }
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

age_column = df['Age']
print("\nAge Column:")
print(age_column)

second_row = df.iloc[1]
print("\nSecond Row:")
print(second_row)

subset =df.loc[0:2, ['Name', 'Age']]
print("\nSubset (First 3 rows, Name and Age columns):")
print(subset)

filter_data = df[df['Age'] > 25]
print("\nRows where Age > 25:")
print(filter_data)

salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)