import csv

total = 0
valid_age = 0

with open("data_quality_check1/cleaned_final_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += 1
        if int(row["age"]) > 0:
            valid_age += 1

print("Data Summary")
print("------------")
print("Total records:", total)
print("Valid age records:", valid_age)
