import requests 
import pandas as pd
from prettytable import PrettyTable

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
df_users = pd.DataFrame([{
     "UserID": u["id"],
    "Name": u["name"],
    "Username": u["username"],
    "Email": u["email"],
    "City": u["address"]["city"]

} for u in users]) 

posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
df_posts = pd.DataFrame([{
    "PostID": p["id"],
    "UserID": p["userId"],
    "Title": p["title"],
    "Body": p["body"]
} for p in posts])

albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()
df_albums = pd.DataFrame([{
    "AlbumID": a["id"],
    "UserID": a["userId"],
    "Title": a["title"]
} for a in albums])

comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()
df_comments = pd.DataFrame([{
    "CommentID": c["id"],
    "PostID": c["postId"],
    "Name": c["name"].strip().title(),
    "Email": c["email"].lower().strip(),
    "Body": c["body"].strip()
} for c in comments])

# merge users with posts

df_merged = pd.merge(df_users, df_posts, on="UserID", how="left")

# merge the result with comments
df_merged = pd.merge(df_merged, df_comments, on="PostID", how="left", )
# merge the result with albums
df_merged = pd.merge(df_merged, df_albums, on="UserID", how="left", )

df_merged.to_excel("merged_data.xlsx", index=False)
print("Merged data saved to 'merged_data.xlsx'")

df_merged.to_csv("merged_data.csv", index=False)
print("Merged data saved to 'merged_data.csv'")

table = PrettyTable()
table.field_names = df_merged.columns.tolist()
for index, row in df_merged.iterrows():
    table.add_row(row.tolist())

print("Merged Data:")



