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

bad_records = df[df.isnull().any(axis=1)]
good_records = df[~df.isnull().any(axis=1)]

df["name"] = df["name"].fillna("not provided")
df["city"] = df["city"].fillna("unknown")
df["email"] = df["email"].fillna("abc@gmail.com")

df = df.drop_duplicates(subset=["user_id"], keep="last")

invalid_email = ~df["email"].str.contains("@")
df.loc[invalid_email, "email"] = "invalid@unknown.com"

df["is_valid"] = df.notnull().all(axis=1)
