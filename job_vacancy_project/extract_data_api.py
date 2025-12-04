import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
raw_data = response.json()

df = pd.DataFrame(raw_data)
print(df.head())

df = df.rename(columns={
    "userId": "company_id",
    "id": "job_id",
    "title": "job_title",
    "body": "job_description"
})

df["description_length"] = df["job_description"].apply(lambda x: len(x))

df_clean = df.drop_duplicates()
df_clean = df_clean[df_clean["description_length"]>20]
print(df_clean.info())