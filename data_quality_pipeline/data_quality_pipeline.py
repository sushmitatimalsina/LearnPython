import csv

file_name = "data_quality_pipeline/cleaned_final_data.csv"

total_rows = 0
invalid_age_count = 0
unknown_city_count = 0
city_count = {}
ids_seen = set()
duplicate_ids = set()

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_rows += 1

        # Check invalid age
        if int(row["age"]) == 0:
            invalid_age_count += 1

        # Check unknown city
        if row["city"] == "Unknown":
            unknown_city_count += 1

        # Count by city
        city = row["city"]
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

        # Check duplicate IDs
        if row["id"] in ids_seen:
            duplicate_ids.add(row["id"])
        else:
            ids_seen.add(row["id"])

# -------- REPORT --------
print("\nDATA QUALITY REPORT")
print("-------------------")
print("Total records:", total_rows)
print("Invalid age records (age = 0):", invalid_age_count)
print("Unknown city records:", unknown_city_count)
print("Duplicate IDs:", duplicate_ids)

print("\nRecords per city:")
for city, count in city_count.items():
    print(f"{city}: {count}")
