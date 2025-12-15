import pandas as pd
import csv

with open("output.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["order_id"], row["amount"], row["country"])
