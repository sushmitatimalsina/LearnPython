import csv

input_file = "data_engineer_cleaning/raw_data.csv"
output_file = "data_engineer_cleaning/cleaned_final_data.csv"

# Mapping text age to number
age_map = {
    "twenty": "20"
}

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        age = row["age"].strip().lower()

        # Convert word age to number
        if age in age_map:
            row["age"] = age_map[age]
        elif age.isdigit():
            row["age"] = age
        else:
            row["age"] = "0"

        # Fix empty city
        if row["city"].strip() == "":
            row["city"] = "Unknown"

        writer.writerow(row)

print("Age words converted and data cleaned successfully")
