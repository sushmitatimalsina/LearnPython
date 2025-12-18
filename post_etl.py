import requests
import pymysql

def extract_posts():
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print("API error:", e)
        return []

def transform_posts(data):
    posts = []
    for post in data:
        posts.append((
            post["id"],
            post["userId"],
            post["title"],
            post["body"]
        ))
    return posts

def load_posts(posts):
    if not posts:
        print("No posts to load")
        return

    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root123",
            database="testdb"
        )
        cursor = conn.cursor()

        for post in posts:
            cursor.execute(
                """
                INSERT INTO posts (post_id, user_id, title, body)
                VALUES (%s, %s, %s, %s)
                """,
                post
            )

        conn.commit()
        conn.close()
        print("Posts ETL completed successfully")

    except Exception as e:
        print("DB error:", e)

def run_etl():
    data = extract_posts()
    print("Fetched records:", len(data))  # DEBUG
    posts = transform_posts(data)
    load_posts(posts)

run_etl()
