import pymysql

def get_mysql_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root123",
            database="testdb"
        )

        print("Connected to MySQL successfully")
        return conn

    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)
        return None

conn = get_mysql_connection()

def create_table(conn):
    try:
        cursor= conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS students(
        id INT  AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        city VARCHAR(50)
        )
        """
        cursor.execute(query)
        print("Table 'students' created successfully")
    except pymysql.MySQLError as e:
        print("create table error:", e)
    finally:
        cursor.close()



if conn:
    create_table(conn)
    conn.close()
    print("MySQL connection closed")


