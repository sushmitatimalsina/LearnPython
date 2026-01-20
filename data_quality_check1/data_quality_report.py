import csv

file_name = "data_quality_check1/cleaned_final_data.csv"

total_rows = 0
invalid_age_count = 0
unknown_city_count = 0

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_rows += 1

        if int(row["age"]) == 0:
            invalid_age_count += 1

        if row["city"] == "Unknown":
            unknown_city_count += 1

print("Data Quality Report")
print("-------------------")
print("Total rows:", total_rows)
print("Rows with invalid age:", invalid_age_count)
print("Rows with unknown city:", unknown_city_count)
