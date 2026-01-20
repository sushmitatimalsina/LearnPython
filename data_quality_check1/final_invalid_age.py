import csv

with open("data_quality_check1/cleaned_final_data.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Rows with invalid age:")
    for row in reader:
        if int(row["age"]) == 0:
            print(row)
