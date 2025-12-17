import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="testdb"
    )

    print("Connected to MySQL successfully")

    conn.close()

except Exception as e:
    print("Error:", e)
