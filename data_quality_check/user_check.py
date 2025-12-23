import pandas as pd

df = pd.read_csv("users_clean1.csv")

print("null value")
print(df.isnull().sum())