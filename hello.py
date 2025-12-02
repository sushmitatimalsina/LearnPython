# print ("hello Sushmita!")
# print("Python is working!")

# print(123)
# print(1+2)

# print('hello')
# print("a"+"b")
# print("1"+"a")

# # addition
# print(1+2)

# # subtraction
# print(1-2)

# # multiplication
# print(5*5)

# # division
# print(8/2)

# # exponent -(we use **  to denote exponents)
# print(2**3)

# # modulus (remainder)-%
# print(6%2)
# print(3%2)

# print(5-10+5)
# print(-100+20+5)

# name="sushmita"
# print(name)
# print('Timalsina')

# # num1="12"
# # num2=3
# # # print(num1/num2)

# print(type("ram"))
# print(type(name))

# # print(a)

# name = "Sushmita Timalsina"
# age = 32
# percentage = 80.55
# address = "Kathmandu"

# print(name, age, percentage, address)
# print("My name is ", name)
# print("My name is ", name, "I am ", age, " years old.", percentage, address)

# print(f"My name is {name}. I am {age} years old. I live in {address}.")

# type(name)

# age = 23
# print("Age 1", age)
# print("Age 2", age)
# age = 34
# print("Age 3",age)


# a = 10
# b = 20
# # Floor Division:
# #  division that rounds the result down to the nearest whole number, effectively discarding any fractional part
# print(a//b)

# x=15
# x+=5
# print(x)

# x/=5
# print(x)

# x%=5
# print(x)

# m = 10.0
# n = 20
# print("Equal:", m == n)
# print("Not Equal:", m != n)
# print("Greater than:", m > n)
# print("Less than:", m < n)

# s = "hello"

# print("Equal:", m == s)

# print(type(m))
# h = int(a) ## explicit type conversion
# print(type(h))

# age = 20
# has_id = True
# print("Can vote:", age >= 18 and has_id)

# # name = input("Enter your name:")
# # age = input("Enter your age:")
# # print(name, age)
# # print(f"{name} was born in {2025-int(age)}.")


# l, p, d = "hi" ,11, 5.6
# print(l, p, d)

# fruits = ["apple", "banana", "cherry"]
# e, t, r = fruits
# print(e, t, r)

# # x = "Python "
# # y = "is "
# # z = "awesome"
# # print(x + y + z)

# # j = "awesome"
# # def myfunc():
# #     print("python is " + j)
# #     myfunc()

# address = "Kathmandu"
# print(len(address))

# txt = "The best things in life are free!"
# # print("free" in txt)

# if "khusi" in txt:
#   print("Yes, 'free' is present.")

#   print(txt[7:11])

# fname = input("Enter your name: ")
# print("Hello,", fname)

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
print(matrix)

random_numbers = np.random.randint(1, 100, size=(3,3))
print(random_numbers)

random_nums = np.random.randint(1, 100, size=5)
print(random_nums)

arr = np.array([10, 20, 30])
result = arr * 2
print(result)