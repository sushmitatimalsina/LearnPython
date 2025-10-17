import csv

Data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 22, "Chicago"]

]

with open ("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(Data) 

print("csv file has been written successfully")    
