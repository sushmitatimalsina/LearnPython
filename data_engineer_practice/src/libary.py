import csv

with open("data_engineer_practice/data/library.csv", "r") as file:
    records = csv.DictReader(file)
    clean_records = []

    for r in records:
        if r["student_id"] != "0":
            if r["return_date"] == "":
                r["return_date"] = "Not Returned"
            clean_records.append(r)

with open("data_engineer_practice/data/clean_library.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["book_id", "book_name", "student_id", "issue_date", "return_date"]
    )
    writer.writeheader()
    writer.writerows(clean_records)

print("Clean library data saved")
