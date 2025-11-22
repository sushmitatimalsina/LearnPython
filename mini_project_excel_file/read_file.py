import pandas as pd

df = pd.read_excel(r"D:\python\python\mini_project_excel_file\customer.xlsx")
print("Original Data:")
print(df)

filtered = df[df["Age"] > 23]
print(filtered)