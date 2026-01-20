import csv

ids = set()
duplicates = set()

with open("data_quality_check1/cleaned_final_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["id"] in ids:
            duplicates.add(row["id"])
        else:
            ids.add(row["id"])

print("Duplicate IDs found:", duplicates)
