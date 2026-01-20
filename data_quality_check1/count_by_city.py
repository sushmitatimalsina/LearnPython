import csv

city_count = {}

with open("data_quality_check1/cleaned_final_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]

        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

print("Students count by city:")
for city, count in city_count.items():
    print(city, ":", count)
