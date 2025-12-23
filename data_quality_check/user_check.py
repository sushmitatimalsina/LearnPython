import pandas as pd

df = pd.read_csv("users_clean1.csv")

print("null value")
print(df.isnull().sum())

print("duplicate value")
print(df.duplicated().sum())

df_no_duplicates = df.drop_duplicates()
print("after removing duplicate:")
print(df_no_duplicates)

df_clean = df_no_duplicates.dropna()
print("after removing null values:")
print(df_clean)