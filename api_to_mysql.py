import requests
import pymysql

def etl_api_to_mysql():
    # Extract
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    
    print(f"Fetched {len(data)} users from API")  # Debug

    # Connect to MySQL
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="testdb"
    )
    cursor = conn.cursor()

    # Transform + Load
    for user in data:
        print(f"Inserting user: {user['name']}")  # Debug
        cursor.execute(
            """
            INSERT INTO users (id, name, email, phone)
            VALUES (%s, %s, %s, %s)
            """,
            (user["id"], user["name"], user["email"], user["phone"])
        )

    conn.commit()
    conn.close()
    print("ETL completed: API data inserted into MySQL")

etl_api_to_mysql()


