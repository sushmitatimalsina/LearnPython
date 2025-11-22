import pandas as pd

# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)    

df = pd.read_excel(r"D:\python\python\file_handling\output.xlsx")
print(df)