import csv
import json

users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Alice", "email": "alice@example.com"}
]

for user in users:
    print(f"{user['id']} - {user['name']} - {user['email']}")

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "email"])
    writer.writeheader()
    writer.writerows(users)

with open("users.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)