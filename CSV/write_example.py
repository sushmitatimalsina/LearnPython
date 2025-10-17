import csv

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 22, "City": "Chicago"}
]

fieldnames = ["Name", "Age", "City"]

with open ("output_dict.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


print("CSV file (dictionary style) has been written successfully!")    