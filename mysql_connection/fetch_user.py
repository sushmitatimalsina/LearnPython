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
conn = get_mysql_connection()
