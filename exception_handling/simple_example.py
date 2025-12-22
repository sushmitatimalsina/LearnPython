# try:
#     number = int("10")
#     print("Number converted")

# except ValueError:
#     print("Conversion failed")

# else:
#     print("This runs because no error occurred")

# try:
#     number = int("abc")

# except ValueError:
#     print("Conversion failed")

# else:
#     print("No error occurred")   

try:
    result = 10 / 2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
