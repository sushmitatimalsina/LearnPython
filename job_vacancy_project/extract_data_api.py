import requests
import pandas as pd
import mysql.connector

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

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="job_data"
)

cursor = conn.cursor()
for _, row in df_clean.iterrows():
    cursor.execute("""
        INSERT INTO jobs (job_id, company_id, job_title, job_description, description_length)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()

print("\nData loaded into MySQL successfully!")
