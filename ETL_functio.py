import requests
import pymysql

# def etl_api_to_mysql():
#     try:
#         # Extract
#         url = "https://jsonplaceholder.typicode.com/users"
#         response = requests.get(url)
#         data = response.json()
#         print(f"Fetched {len(data)} users from API")

#         # Connect to MySQL
#         conn = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="root123",
#             database="testdb"
#         )
#         cursor = conn.cursor()

#         # Transform + Load
#         for user in data:
#             try:
#                 cursor.execute(
#                     """
#                     INSERT INTO users (id, name, email, phone)
#                     VALUES (%s, %s, %s, %s)
#                     ON DUPLICATE KEY UPDATE
#                         name = VALUES(name),
#                         email = VALUES(email),
#                         phone = VALUES(phone)
#                     """,
#                     (user["id"], user["name"], user["email"], user["phone"])
#                 )
#                 print(f"Inserted/Updated user: {user['name']}")
#             except Exception as e:
#                 print(f"Error inserting user {user['name']}: {e}")

#         conn.commit()
#         print("ETL completed: API data inserted/updated in MySQL")

#     except Exception as e:
#         print(f"ETL failed: {e}")

#     finally:
#         if 'conn' in locals() and conn.open:
#             conn.close()

# # Run ETL
# etl_api_to_mysql()

API_URL = "https://jsonplaceholder.typicode.com/users"
DB_CONFIG ={
    "host": "localhost",
    "user": "root",
    "password": "root123",
    "database": "testdb"
}

def extract_data():
    print("Extracting data from API...")
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def transform_data(data):
    print("Transform data ...")
    transformed = []
    for user in data:
        transformed.append((
            user["id"],
            user["name"],
            user["email"],
            user["phone"]
        ))
    return transformed

def load_data(data):
    print("Loading data into MySQL...")
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = """
        INSERT INTO users (id, name, email, phone)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            email = VALUES(email),
            phone = VALUES(phone)
    """

    cursor.executemany(query, data)
    conn.commit()
    conn.close()

def run_etl():
    try:
        raw_data = extract_data()
        print(f"Fetched {len(raw_data)} records")

        clean_data = transform_data(raw_data)

        load_data(clean_data)

        print("ETL pipeline completed successfully")

    except Exception as e:
        print("ETL pipeline failed:", e)

run_etl()