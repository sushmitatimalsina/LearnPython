import requests
import pandas as pd
from prettytable import PrettyTable

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

# url = "https://jsonplaceholder.typicode.com/posts"
# response  = requests.get(url)
# data = response.json()
# print(data[0])

# posts = []
# for item in data:
#     posts.append({
#         "UserID": item["userId"],
#         "PostID": item["id"],
#         "Title": item["title"],
#         "Body": item["body"]
#     })

# df = pd.DataFrame(posts)
# print(df)
# df.to_csv("api_posts.csv", index=False)
# print("Data saved to 'api_posts.csv'")  

# url = "https://jsonplaceholder.typicode.com/comments"
# response = requests.get(url)
# data = response.json()
# print(data[0])

# comments = []
# for item in data:
#     comments.append({
#         "PostID": item["postId"],
#         "CommentID": item["id"],
#         "Name": item["name"].strip().title(),
#         "Email": item["email"].lower().strip(),
#         "Body": item["body"].strip()
#     })

# df = pd.DataFrame(comments)
# print(df)
# df.to_json("api_comments.json", orient="records", lines=True)
# print("Data saved to 'api_comments.json'")


# df_html = df.to_html()
# with open("api_comments.html", "w") as file:
#     file.write(df_html)
# print("Data saved to 'api_comments.html'")
# df.to_excel("api_comments.xlsx", index=False)
# print("Data saved to 'api_comments.xlsx'")

# df = pd.DataFrame(comments)

# df = df.drop_duplicates()

# df.to_json("clean_api_comments.json", orient="records", lines=True)

# url = "https://jsonplaceholder.typicode.com/albums"
# response = requests.get(url)
# data = response.json()
# print(data[0])

# albums = []
# for item in data:
#     albums.append({
#         "UserID": item["userId"],
#         "AlbumID": item["id"],
#         "Title": item["title"].strip().title()
#     })

# df = pd.DataFrame(albums)
# print(df)
# df.to_csv("api_albums.csv", index=False)
# print("Data saved to 'api_albums.csv'")

# df.to_excel("api_albums.xlsx", index=False)
# print("Data saved to 'api_albums.xlsx'")



# table = PrettyTable()
# table.field_names = ["UserID", "AlbumID", "Title"]

# for _, row in df.iterrows():
#     table.add_row([row["UserID"], row["AlbumID"], row["Title"]])

# print(table)


# # df.to_json("api_albums.json", orient="records", lines=True)
# # print("Data saved to 'api_albums.json'")

# df.to_excel("api_albums.xlsx", index=False)
# print("Data saved to 'api_albums.xlsx'")


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(data)

