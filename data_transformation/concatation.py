import pandas as pd

# Two datasets
df1 = pd.DataFrame({'Name': ['Aarav', 'Bina'], 'Salary': [50000, 60000]})
df2 = pd.DataFrame({'Name': ['Chirag', 'Diya'], 'Salary': [55000, 58000]})

# Concatenate vertically (add rows)
concat_df = pd.concat([df1, df2], ignore_index=True)
print(concat_df)