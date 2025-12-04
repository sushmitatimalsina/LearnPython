# # # import pandas as pd
# # # import mysql.connector
# # # import os

# # # # Connect to MySQL
# # # connection = mysql.connector.connect(
# # #     host="localhost",
# # #     user="root",
# # #     password="",
# # #     database="sushmita_practice"
# # # )

# # # # SQL query
# # # query = "SELECT * FROM student"

# # # # # Load data into DataFrame
# # # df = pd.read_sql(query, connection)
# # # print(df)

# # # # # Save to CSV
# # # file_name = "mysql_student.csv"
# # # df.to_csv(file_name, index=False)

# # # # # Print exact file path
# # # full_path = os.path.abspath(file_name)
# # # print("\nData saved to:", full_path)

# # # # # Close connection
# # # connection.close()


# # import mysql.connector
# # from prettytable import PrettyTable

# # # Connect to MySQL
# # connection = mysql.connector.connect(
# #     host="localhost",     # Database host
# #     user="root",          # MySQL username
# #     password="",          # MySQL password
# #     database="xyz"    # Database name
# # )

# # cursor = connection.cursor()

# # # Write your SQL query
# # query = "SELECT * FROM address"

# # cursor.execute(query)

# # # Fetch all rows
# # results = cursor.fetchall()

# # # Print result
# # for row in results:
# #     print(row)


# # table = PrettyTable(["address_id", "address", "City_id", "postal_code", "phone"])
# # for row in results:
# #     table.add_row(row)

# # print(table)

# # connection.close()


# import mysql.connector
# from prettytable import PrettyTable

# try:
#     # Connect to MySQL
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",       # enter password if you have one
#         database="xyz"     # your database name
#     )

#     print("Connected to MySQL successfully!")

#     cursor = connection.cursor()

#     # Fetch data from book_details table
#     query = "SELECT * FROM book_details"
#     cursor.execute(query)

#     results = cursor.fetchall()

#     # Display data in table format
#     table = PrettyTable(["Book ID", "Book Name", "Author Name", "Category", "Total Copies", "Available Copies", "Publish Year"])

#     for row in results:
#         table.add_row(row)

#     print("\n📘 Book Details Data:")
#     print(table)

# except Exception as e:
#     print("❌ Error:", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("\nMySQL connection closed")


import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="xyz"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM book_details")

for row in cursor.fetchall():
    print(row)

connection.close()
input("PRESS ENTER TO EXIT")
