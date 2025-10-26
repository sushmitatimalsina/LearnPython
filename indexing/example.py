import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 26],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

indexed_df = df.set_index('Name')
print("\nDataFrame with 'Name' as index:\n", indexed_df)

reset_df = indexed_df.reset_index()
print("\nDataFrame after resetting index:\n", reset_df)

# Select one row by label
print(indexed_df.loc['Bob'])
print("======")
# Select specific rows and columns
print(indexed_df.loc[['Alice', 'Eva'], ['Age']])