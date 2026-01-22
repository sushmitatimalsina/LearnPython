import csv

# Read users data
with open("data_engineer_practice/data/users.csv", "r") as file:
    reader = csv.DictReader(file)
    users = list(reader)

city_count = {}

# Count users per city (ignore empty city)
for user in users:
    city = user["city"].strip()
    if city:
        city_count[city] = city_count.get(city, 0) + 1

# Write result to CSV
with open("data_engineer_practice/data/city_counts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["city", "total_users"])
    for city, count in city_count.items():
        writer.writerow([city, count])

print("City-wise user count saved to data/city_counts.csv")
