import csv

with open("data_quality_check1/cleaned_final_data.csv", "r") as infile, open("data_quality_check1/valid_age_data.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

    writer.writeheader()

    for row in reader:
        if int(row["age"]) > 0:
            writer.writerow(row)

print("Valid age data saved to valid_age_data.csv")
