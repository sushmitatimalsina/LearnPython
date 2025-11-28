import pandas as pd

# Create a dictionary of data
# data = {
#     'Name': ['Sita', 'Gita', 'Hari', 'Rita'],
#     'Age': [25, 30, 22, 28],
#     'Department': ['HR', 'Finance', 'IT', 'Marketing'],
#     'Salary': [40000, 50000, 45000, 48000]
# }

# # Convert the dictionary into a DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)

# import pandas as pd

# # Create a simple DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 22],
#     'City': ['Kathmandu', 'Pokhara', 'Lalitpur']
# }

# df = pd.DataFrame(data)
# print(df)

data = {
    'City': ['Kathmandu', 'Kathmandu', 'Pokhara', 'Pokhara'],
    'Sales': [200, 300, 150, 400]
}

df = pd.DataFrame(data)

# Group by city and sum sales
grouped = df.groupby('City')['Sales'].sum()
print(grouped)
