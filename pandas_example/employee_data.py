import pandas as pd

data = {
     "name": ["Sushmita", "Ramesh", "Anita", "Kiran", "Sabina"],
    "age": [25, 30, 28, 35, 27],
    "city": ["Kathmandu", "Pokhara", "Biratnagar", "Kathmandu", "Pokhara"],
    "salary": [50000, 60000, 55000, 70000, 52000]
}

df = pd.DataFrame(data)
print("full data Frame:")
print(df)

high_salary = df[df["salary"] > 55000]
print("\nEmployees with salary greater than 55000:")
print(high_salary)

avg_age = df["age"].mean()
print("\nAverage age of employees:", avg_age)