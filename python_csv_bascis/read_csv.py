import csv

# Open the CSV file
with open("python_csv_bascis/data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
