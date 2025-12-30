import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(f"Fetched {len(data)} users from API")
df = pd.DataFrame(data)
df = df[["id", "name", "email", "address"]]
# df["city"] = df["address"].apply(lambda x: x["city"])
# df = df.drop(columns=["address"])

# print("\nRaw data:")
# print(df.head())