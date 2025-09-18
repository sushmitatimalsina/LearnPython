import numpy as np
import array as arr


fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[2])
fruits.append("orange")
print(fruits)

nums = np.array([1, 2, 3, 4, 5])
print(nums * 2) 

number = [1,2,3,4,5]
print(number * 2)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

arry = arr.array('d',[1.1, 1.2, 1.3,])
print(arry[1])
arry.append(1.4)
print(arry)
for x in arry:
    print(x)
print("=====")
for y in arry[1:3]:
    print(y)

questions = ['name', 'address', 'favorite color']
answers = ['sushmita ', 'banepa', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)     


basket = ['apple', 'orange', 'pear', 'orange', 'banana']   
for f in sorted(basket):
    print(f)
    print("====")
for s in sorted(set(basket)):
    print(s)    
    

my_array = [7, 8, 9 ,4, 5, 1, 0]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i
print("min Value is ", minVal)

n = len(my_array)

for m in range(n-1):
    for k in range(n-m-1):
        if my_array[k] > my_array[k + 1]:
            my_array[k], my_array[k + 1] =  my_array[k + 1] , my_array[k]

print("Sorted array:", my_array)


