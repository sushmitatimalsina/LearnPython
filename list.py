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
    
