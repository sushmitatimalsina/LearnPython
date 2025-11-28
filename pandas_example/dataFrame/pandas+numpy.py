import pandas as pd
import numpy as np

arr = np.random.randint(1, 10, size=(4, 3))
df = pd.DataFrame(arr, columns=["A", "B", "C"])
print("DataFrame created from NumPy array:")
print(df)

# Perform basic statistical operations
print("\nStatistical Summary:")
print(df.describe())

# Add a new column with the mean of each row
df['Mean'] = df.mean(axis=1)
print("\nDataFrame with Mean column:")
print(df)

array_data = df["B"].to_numpy()
print("\nNumPy array from column B:")
print(array_data)

df["Category"] = np.where(df["A"] > 5, "High", "Low")
print("\nDataFrame with Category column based on values in column A:")
print(df)