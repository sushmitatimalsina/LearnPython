import csv

input_file = "data_engineer_cleaning/raw_data.csv"
output_file = "data_engineer_cleaning/cleaned_data.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Handle missing age
        if row["age"] == "" or row["age"] is None:
            row["age"] = "0"

        # Handle missing city
        if row["city"] == "" or row["city"] is None:
            row["city"] = "Unknown"

        writer.writerow(row)

print("Data cleaned and saved to cleaned_data.csv")
