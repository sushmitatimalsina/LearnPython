import pandas as pd

df = pd.read_excel(r"D:\python\python\customer.xlsx")
print("Original Data:")
print(df)
print("-----------------")

filtered = df[df["Age"] > 23]
print(filtered)

print("-----------------")
cleaned = filtered.dropna(subset=["Age"])
print(cleaned)