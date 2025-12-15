import pandas as pd
import csv
import json

# with open("output.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["order_id"], row["amount"], row["country"])


with open("countries.json", "r") as file:
    data = json.load(file)

countries = data["countries"]
with open("countries_converted.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["country"])  # Header
    for c in countries:
        writer.writerow([c])    