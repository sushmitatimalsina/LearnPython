import pandas as pd
import mysql.connector
import os

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sushmita_practice"
)

# SQL query
query = "SELECT * FROM student"

# # Load data into DataFrame
df = pd.read_sql(query, connection)
print(df)

# # Save to CSV
file_name = "mysql_student.csv"
df.to_csv(file_name, index=False)

# # Print exact file path
full_path = os.path.abspath(file_name)
print("\nData saved to:", full_path)

# # Close connection
connection.close()
