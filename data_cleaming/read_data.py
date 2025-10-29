import pandas as pd

df = pd.read_csv('output_dict.csv')
print("Original DataFrame:\n", df)
print("======")
# Display the first few rows of the DataFrame

print(df.head())
print("======")
# Display summary statistics of the DataFrame
print(df.describe())