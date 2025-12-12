import pandas as pd

# def my_function():

#  print("hello ")

# # my_function()

# def details(fname):
#     print(fname + " Timalsina")   

# details("Sushmita")
# details("Sushil")
# details("Saraswoti")
# details("Govinda")

# def student(name,sirname):
#     print(name + " " + sirname)

# student("Asmita", "Timalsina")    

# def fruits(*name):
#     print("My fav fruits is " + name[2])
# fruits("apple", "banana", "Mango")

# def child(child3, child2, child1):
#     print("The younger child is " + child3)

# child(child1 = "Emil", child2 = "Tobias", child3 = "Linus")    

# def hi(food):
#     for x in food:
#         print(x)
# game = ("a", "b", "c")
# hi(game)

# def add(x):
#     return 5 + x
# # print(add(5))
# print("Sum is " + str(add(10)))

# def greet(name="User"):
#     return f"Hello, {name}!"
# print(greet()) 
 

# def add_numbers(a, b):
#     return a + b

# print(add_numbers(10, 20))

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1, 2, 3, 4))  # 10

# # # **kwargs: multiple keyword arguments
# # def print_details(**kwargs):
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")

# # print_details(name="Sushmita", age=22, city="Kathmandu")

# # def arithmetic_operations(a, b):
# #     sum_ = a + b
# #     diff = a - b
# #     prod = a * b
# #     return sum_, diff, prod

# # s, d, p = arithmetic_operations(10, 5)
# # print(s, d, p)


# # Example 1: Clean dataframe
# def clean_data(df):
#     df = df.drop_duplicates()
#     df = df.fillna(0)
#     return df

# # Example 2: Filter dataframe by age
# def filter_adults(df):
#     return df[df['age'] >= 18]

# # Example 3: Add new column
# def add_full_name(df):
#     df['full_name'] = df['first_name'] + " " + df['last_name']
#     return df

# # Usage
# df = pd.DataFrame({
#     'first_name': ['John', 'Jane'],
#     'last_name': ['Doe', 'Smith'],
#     'age': [17, 22]
# })

# df = clean_data(df)
# df = filter_adults(df)
# df = add_full_name(df)
# print(df)

# # Simple lambda
# square = lambda x: x**2
# print(square(5))  # 25

# # Lambda inside map
# numbers = [1, 2, 3, 4]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)  # [1, 4, 9, 16]


# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Minor"

# print(check_age(20))
# print(check_age(12))

# def filter_even(numbers):
#     return [n for n in numbers if n % 2 == 0]

# print(filter_even([1, 2, 3, 4, 5, 6]))

def greet():
    print("Hello! Welcome to Python.")
greet()

def say_hello(name):
    print("Hello", name)
say_hello("Sushmita")

def add(a, b):
    return a + b
result = add(5, 10)
print("Sum is:", result)