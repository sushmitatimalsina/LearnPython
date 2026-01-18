import csv

input_file = "data_engineer_cleaning/raw_data.csv"
output_file = "data_engineer_cleaning/cleaned_age_data.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        age = row["age"].strip()

        # Fix wrong age values
        if age.isdigit():
            row["age"] = age
        else:
            row["age"] = "0"

        # Fix missing or blank city
        if row["city"] is None or row["city"].strip() == "":
            row["city"] = "Unknown"

        writer.writerow(row)

print("Age data type cleaned and saved to cleaned_age_data.csv")
