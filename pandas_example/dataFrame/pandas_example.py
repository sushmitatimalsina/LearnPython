import pandas as pd

# # data = {
# #     "Name":[ "John", "Anna", "Peter", "Linda" ],
# #     "Age":[ 28, 24, 35, 32 ],
# #     "City":[ "New York", "Paris", "Berlin", "London" ],
# #     "salary": [50000, 60000, 55000, 65000]

# # }
# # df = pd.DataFrame(data)
# # print(df)

# # print("===========================")
# # print(df.head(2))  # First 2 rows
# # print("===========================")
# # print(df.tail(2))  # Last 2 rows

# data = {
#     "Name": ["Ram", "Sita", "Hari"],
#     "Age": [25, 22, 28],
#     "City": ["Kathmandu", "Pokhara", "Lalitpur"]
# }

# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("new_students.csv")
# print(df.head())



data = {
    "user_id": [1, 2, 3, 4, 5],
    "name": ["Sushmita", "Alex", "Priya", "John", "Mina"],
    "email": [
        "sushmita@example.com",
        "alex@example.com",
        "priya@example.com",
        "john@example.com",
        "mina@example.com"
    ],
    "age": [23, 30, 27, None, 25],
    "city": ["Kathmandu", "Pokhara", "Butwal", "Kathmandu", None]
}

df = pd.DataFrame(data)

print(df)


