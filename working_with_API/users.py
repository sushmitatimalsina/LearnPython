import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# print("Fetched Data:")
# table = pd.DataFrame([{
#     "UserID": u["id"],
#     "Name": u["name"].strip().title(),
#     "Username": u["username"].strip(),
#     "Email": u["email"].lower().strip(),
#     "City": u["address"]["city"].strip().title()
# } for u in data])
# print(table)

df = pd.DataFrame(data)
df = df[["id", "name", "email", "phone"]]
df = df.rename(columns={"name": "user_name"})
df = df.drop_duplicates()


