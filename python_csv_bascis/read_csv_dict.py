import csv

with open("python_csv_bascis/data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
