import mysql.connector

def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="testdb"
        )

        if conn.is_connected():
            print("Connected to MySQL successfully")
            return conn

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)
        return None
    
