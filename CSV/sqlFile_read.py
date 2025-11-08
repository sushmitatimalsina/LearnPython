# file_path = 'employee.sql'

# with open(file_path, 'r', encoding='utf-8') as file:
#     sql_content = file.read()

# print("SQL file content:")
# print(sql_content)

# file_path = "D:\SQL\sql_practice\sastosaman.sql"
# with open(file_path, 'r', encoding='utf-8') as file:
#     sql_content = file.read()

# print(sql_content)
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # your MySQL password
    database="sastosaman"  # your database
)

cursor = conn.cursor()

# Read the SQL file
with open(r"D:\SQL\sql_practice\sastosaman.sql", 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Execute all SQL statements safely
try:
    for result in cursor.execute(sql_script, multi=True):
        pass  # iterates through all statements
except mysql.connector.Error as e:
    print(f"Error executing SQL: {e}")

conn.commit()
cursor.close()
conn.close()

print("✅ SQL file executed successfully!")

