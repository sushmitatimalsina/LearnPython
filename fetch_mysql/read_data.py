import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sastosaman"
)

query = "SELECT * FROM customer"
df = pd.read_sql(query, connection)
print(df)
df.to_csv("mysql_customers.csv", index=False)
print("Data saved to 'mysql_customers.csv'")
connection.close()