import pandas as pd

# data = {
#     "Name":[ "John", "Anna", "Peter", "Linda" ],
#     "Age":[ 28, 24, 35, 32 ],
#     "City":[ "New York", "Paris", "Berlin", "London" ],
#     "salary": [50000, 60000, 55000, 65000]

# }
# df = pd.DataFrame(data)
# print(df)

# print("===========================")
# print(df.head(2))  # First 2 rows
# print("===========================")
# print(df.tail(2))  # Last 2 rows

data = {
    "Name": ["Ram", "Sita", "Hari"],
    "Age": [25, 22, 28],
    "City": ["Kathmandu", "Pokhara", "Lalitpur"]
}

df = pd.DataFrame(data)
print(df)