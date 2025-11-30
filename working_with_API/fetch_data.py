import requests
import pandas as pd

# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# data = response.json()
# print(data[0])

# users = []

# for item in data:
#     users.append({
#         "ID": item["id"],
#         "Name": item["name"],
#         "Username": item["username"],
#         "Email": item["email"],
#         "City": item["address"]["city"]
#     })

# df = pd.DataFrame(users)
# print(df)

# df.to_excel("api_users.xlsx", index=False)
# print("Data saved to 'api_users.xlsx'")

url = "https://jsonplaceholder.typicode.com/posts"
response  = requests.get(url)
data = response.json()
print(data[0])

posts = []
for item in data:
    posts.append({
        "UserID": item["userId"],
        "PostID": item["id"],
        "Title": item["title"],
        "Body": item["body"]
    })

df = pd.DataFrame(posts)
print(df)
df.to_csv("api_posts.csv", index=False)
print("Data saved to 'api_posts.csv'")  

