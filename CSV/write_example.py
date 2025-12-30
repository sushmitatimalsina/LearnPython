import csv
import pandas as pd

# data = [
#     {"Name": "Alice", "Age": 25, "City": "New York"},
#     {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
#     {"Name": "Charlie", "Age": 22, "City": "Chicago"},
#     {"Name": "Alice", "Age": 25, "City": "New York"},
#     {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
#     {"Name": "Charlie", "Age": 22, "City": "Chicago"}

# ]

# fieldnames = ["Name", "Age", "City"]

# with open ("output_dict.csv", mode="w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)


# print("CSV file (dictionary style) has been written successfully!")   
# 
data = {
    "user_id": [1, 2, 2, 3, 4],
    "name": ["Ram", "Sita", "Sita", None, "Hari"],
    "city": ["Kathmandu", "Banepa", "Banepa", "Pokhara", None]
}

df = pd.DataFrame(data)
print("Original data:")
print(df) 

df = df.drop_duplicates(subset=["user_id"])
print("\nAfter removing duplicates:")
print(df)