import pymysql
import requests

def get_mysql_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user= "root",
            password= "root123",
            database= "testdb"
        )
        print("Connected to MySQL successfully")
        return conn
    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)
        return None


def fetch_api_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        print("Error fetching API data:", e)
        return []
    

def create_table(conn):
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS api_users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        city VARCHAR(50)
        )
        """
        cursor.execute(query)
        print("Table 'api_users' created successfully")


    except pymysql.MySQLError as e:
        print("create table error:", e)

    finally:
        cursor.close()  

def insert_api_data(conn, user):
    try:
        cursor= conn.cursor()
        query = """
        INSERT INTO api_users(name,email,city)
        VALUES(%s,%s,%s)
        """
        for u in user:
            cursor.execute(query,(
                u['name'],
                u['email'],
                u['address']['city']
            )
                           )
        conn.commit()
        print("API data inserted successfully")

    except pymysql.MySQLError as e:
        print("insert api data error:", e)


    finally:
        cursor.close()        

conn = get_mysql_connection()
api_data = fetch_api_data()
if conn:
    create_table(conn)
    insert_api_data(conn, api_data)


conn.close()
print("MySQL connection closed")


