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


def insert_data(conn):
    try:
        cursor= conn.cursor()
        query= """
        INSERT INTO students(name, age,city)
        values
        (%s, %s, %s)

        """

        data = [
            ("sushmita Timalsina", 22, "Banepa")
        ]
        cursor.executemany(query, data)
        conn.commit()
        print("data inserted successfully")
    except pymysql.MySQLError as e:
        print("insert data error:", e)
    finally:
        cursor.close()  

def display_data(conn):
    try:
        cursor= conn.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    except pymysql.MySQLError as e:
        print("display data error:", e)

    finally:
        cursor.close()   

def update_faculty(conn):
    try:
        cursor = conn.cursor()
        query = "ALTER TABLE students ADD COLUMN faculty VARCHAR(100)"
        cursor.execute(query)
        conn.commit()
        print("Column 'faculty' added successfully")

    except pymysql.MySQLError as e:
        print("update faculty error:", e)

    finally:
        cursor.close()        

if conn:
    create_table(conn)
    # insert_data(conn)
    print("Fetched data from book_details table:")
    display_data(conn)
    update_faculty(conn)
    conn.close()
    print("MySQL connection closed")


