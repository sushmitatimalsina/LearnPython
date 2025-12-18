import pandas as pd

# # Create data as a list of lists
# data = [
#     [101, 'Aarav', 'Engineering', 60000],
#     [102, 'Bina', 'HR', 52000],
#     [103, 'Chirag', 'Finance', 58000],
#     [104, 'Diya', 'Marketing', 55000]
# ]

# # Define column names
# columns = ['Employee_ID', 'Name', 'Department', 'Salary']

# # Create the DataFrame
# df = pd.DataFrame(data, columns=columns)

# # Display the DataFrame
# print(df)

data = [
    [1, "Alice", "alice@example.com"],
    [2, "Bob", "bob@example.com"],
    [3, "Charlie", "charlie@example.com"]
]

print(data[0])

print(data[1][1])

for row in data:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

new_row = [4, "David", "david@example.com"]
data.append(new_row)
print(data)

posts_data = [
    [1, 1, "Post 1", "Content 1"],
    [2, 1, "Post 2", "Content 2"],
    [3, 2, "Post 3", "Content 3"]
]

# Load into MySQL (conceptual)
for post in posts_data:
    post_id, user_id, title, body = post
    print(f"Inserting post {post_id} for user {user_id}")


