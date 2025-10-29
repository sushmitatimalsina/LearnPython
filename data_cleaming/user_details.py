import pandas as pd
import numpy as np

data = {
    'Name': [' Alice ', 'Bob', 'Charlie', 'David', 'Eve', 'Alice '],
    'Age': [25, np.nan, 30, 22, 29, 25],
    'City': ['New York', 'los angeles ', 'NEW YORK', np.nan, 'Chicago', 'New York'],
    'Salary': ['50000', '60000', '55000', 'not available', '58000', '50000'],
    'JoinDate': ['2021-01-05', '2020/05/12', '2021-13-10', '2022-07-15', '2021-08-10', '2021-01-05']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

print("\n data info")
print(df.info())

print("\n Check for missing values")
print(df.isnull().sum())