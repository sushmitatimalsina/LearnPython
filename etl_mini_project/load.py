import csv
from extract import extract_sales_data
from transform import transform_data

def load_data():
    raw_data = extract_sales_data()
    clean_data = transform_data(raw_data)

    with open('etl_mini_project/data/clean_sales_data1.csv', mode='w', newline='') as file:
        fieldnames = ["order_id", "product", "quantity", "price", "total_price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(clean_data)

    print("Data loaded into clean_sales_data.csv")
if __name__ == "__main__":
    load_data()