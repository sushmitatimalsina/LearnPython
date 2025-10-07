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

city_group = df.groupby("city")["salary"].mean()
print("\nAverage salary by city:")
print(city_group)

kathmandu_employee = df[df["city"].str.lower() == "kathmandu"]
print("\nEmployees in Kathmandu:")
print(kathmandu_employee)


#  Add a new column for bonus (10% of salary)
df["bonous"] = df["salary"]* 0.1
print("\nData Frame with Bonus column:")
print(df)

avg_salary = df["salary"].mean()
print(f"\nAverage salary: {avg_salary}")

