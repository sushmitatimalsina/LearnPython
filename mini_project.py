import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(f"Fetched {len(data)} users from API")
df = pd.DataFrame(data)
df = df[["id", "name", "email", "address"]]
df["city"] = df["address"].apply(lambda x: x["city"])
df = df.drop(columns=["address"])

print("\nRaw data:")
print(df.head())

df.loc[5, "name"] = None
df.loc[2, "email"] = None
df = pd.concat([df, df.iloc[0:2]])  

print("\nData with duplicates and nulls:")
print(df)
df = df.drop_duplicates(subset=["id"], keep="last")
df["name"] = df["name"].fillna("Unknown")
df["email"] = df["email"].fillna("noemail@unknown.com")

print("\nCleaned data:")
print(df)

df.to_csv("users_final.csv", index=False)
print("\nETL completed! Data saved to users_final.csv")