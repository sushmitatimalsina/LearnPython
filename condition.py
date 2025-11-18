# # a = 33
# # b = 33
# # if b > a:
# #     print("b is grater than a")

# #     # elif- if previous condition werenot true then try this conditions
# # elif a == b:
# #     print("a and b are equal")

# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   if x == "banana":
# #     continue
# #   print(x)

# # for m in range(10):
# #    print(m)
# # else:
# #    print("finally finish")

# # for n in range(2, 30, 3):
# #    if n == 8: continue
# #    print(n)
# # else:
# #    print("finally finished")

# #    adj = ["red", "big", "tasty"]
# #    for j in adj:
# #       for k in fruits:
# #          print(j, k)
# numbers = [12, 45, 7, 23, 89, 5, 33]

# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num 
# print("Maximum number:", max_num)        

# min_num = numbers[0]
# for num1 in numbers:
#     if num1 < min_num:
#         min_num = num1
# print("Minimum number:", min_num)        

# total = 0
# for num2 in numbers:
#       total += num2
# print("Sum of all numbers:", total)    

# sorted_number = numbers.copy()
# for i in range(len(sorted_number)):
#     for j in range(i+1, len(sorted_number)):
#         if sorted_number[i] > sorted_number[j]:
#             sorted_number[i], sorted_number[j] = sorted_number[j], sorted_number[i]
# print("Sorted numbers:", sorted_number)           

# reversed_numbers = []
# for m in range(len(numbers)-1, -1, -1):
#       reversed_numbers.append(numbers[m])
# print("Reversed numbers:", reversed_numbers)  
# 
# if statement
# 
# age = 18
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#        print("You are not eligible to vote.")    

# # if-elif-else statement     
# score = 85
# if score >= 90:
#       print("Grade: A")
# elif score >=80:
#       print("Grade: B") 
# else:
#       print("Grade: C")           

# # Multiple conditions using AND
# num = 15
# if num > 0 and num % 2 == 0:
#     print(f"{num} is a positive even number.")

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
# #     print(x)
#     if x == "banana":
#       #   break
#       continue
#     print(x)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))