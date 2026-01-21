import csv

with open("data_engineer_practice/data/users.csv", "r") as file:
    reader = csv.DictReader(file)
    users = list(reader)

clean_users = []

for user in users:
    if user["age"] != "0":
        clean_users.append(user)

with open("data_engineer_practice/data/clean_users.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clean_users)

print("Clean data saved in data/clean_users.csv")
