import pandas as pd

data = {
    "Name": ["John", "Sita", "Ram"],
    "Age": [24, 22, 26],
    "City": ["Kathmandu", "Pokhara", "Lalitpur"]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)