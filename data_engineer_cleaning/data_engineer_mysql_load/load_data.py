import csv
import pymysql

# MySQL connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root123",
    database="testdb"
)

cursor = connection.cursor()

with open("data_engineer_cleaning/data_engineer_mysql_load/clean_final_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sql = """
        INSERT INTO student_details (id, name, age, city)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            int(row["id"]),
            row["name"],
            int(row["age"]),
            row["city"]
        )
        cursor.execute(sql, values)

connection.commit()
connection.close()

print("Data inserted into MySQL successfully")
