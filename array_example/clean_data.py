# Raw data (not clean)
data = [10, 20, None, 30, None, 40]

# Transform (clean data)
clean_data = []

for value in data:
    if value is not None:
        clean_data.append(value)

# Output
print("Clean Data:", clean_data)