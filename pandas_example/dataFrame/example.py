import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['Sita', 'Gita', 'Hari', 'Rita'],
    'Age': [25, 30, 22, 28],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [40000, 50000, 45000, 48000]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)