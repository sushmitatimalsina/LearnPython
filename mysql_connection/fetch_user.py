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
    
        print("API data fetched successfully")
    except requests.RequestException as e:
        print("Error fetching API data:", e)
        return []
    
conn = get_mysql_connection()
api_data = fetch_api_data()

