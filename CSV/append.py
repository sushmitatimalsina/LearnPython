import csv

new_data = [
    {"Name": "David", "Age": 28, "City": "Miami"},
    {"Name": "Eva", "Age": 26, "City": "Boston"}
]

fieldnames = ["Name", "Age", "City"]

with open("output_dict.csv", mode="a", newline="") as file: 
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerows(new_data)
print("New rows have been appended to the CSV file successfully!")    