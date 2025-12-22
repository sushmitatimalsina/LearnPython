# try:
#     number = int("10")
#     print("Number converted")

# except ValueError:
#     print("Conversion failed")

# else:
#     print("This runs because no error occurred")

try:
    number = int("abc")

except ValueError:
    print("Conversion failed")

else:
    print("No error occurred")   
