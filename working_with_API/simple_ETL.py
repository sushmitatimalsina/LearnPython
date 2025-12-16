import pandas as pd
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

df = pd.DataFrame(data)
df = df[["userId", "title"]]

df.to_csv("posts.csv", index=False)
print("ETL from API completed")

