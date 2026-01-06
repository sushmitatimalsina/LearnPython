import pandas as pd
import pymysql

def get_mysql_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="testdb"
    )

def insert_sales_data(conn):
    df = pd.read_csv("cleaned_sales_data.csv")

    cursor = conn.cursor()

    query = """
        INSERT INTO sales_data
        (order_id, product, quantity, price, quantity_num, price_num, total_price)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = []
    for _, row in df.iterrows():
        data.append((
            int(row["order_id"]),
            row["product"],
            str(row["quantity"]),
            float(row["price"]),
            None if pd.isna(row["quantity_num"]) else float(row["quantity_num"]),
            float(row["price_num"]),
            None if pd.isna(row["total_price"]) else float(row["total_price"])
        ))

    cursor.executemany(query, data)
    conn.commit()
    cursor.close()

    print("Sales data inserted into testdb.sales_data successfully")

if __name__ == "__main__":
    conn = get_mysql_connection()
    insert_sales_data(conn)
    conn.close()
