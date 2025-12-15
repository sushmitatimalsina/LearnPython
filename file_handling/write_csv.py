import pandas as pd
import csv

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "amount", "country"])
    writer.writerow([201, 1500, "Nepal"])
    writer.writerow([202, 2000, "India"])