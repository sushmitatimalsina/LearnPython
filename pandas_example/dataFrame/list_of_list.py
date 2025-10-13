import pandas as pd

# Create data as a list of lists
data = [
    [101, 'Aarav', 'Engineering', 60000],
    [102, 'Bina', 'HR', 52000],
    [103, 'Chirag', 'Finance', 58000],
    [104, 'Diya', 'Marketing', 55000]
]

# Define column names
columns = ['Employee_ID', 'Name', 'Department', 'Salary']

# Create the DataFrame
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)
