# # numbers = [10, 20, 30, 40, 50]
# # print(numbers[0])

# # numbers[2] = 35
# # print(numbers)

# # for num in numbers:
# #     print(num)

# numbers = [10, 20, 30, 40, 50]
# print(numbers)

# print(numbers[0])
# print(numbers[3])  
# numbers.append(60)
# print(numbers)
# numbers.remove(20)
# print(numbers)


import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr)

# Create a 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Array:\n", matrix)

# Basic operations
print("\nArray + 10:", arr + 10)        # add 10 to each element
print("Array * 2:", arr * 2)            # multiply each element by 2
print("Sum of array:", np.sum(arr))     # sum of elements
print("Mean of array:", np.mean(arr))   # average
print("Max of array:", np.max(arr))     # maximum element

print("\nElement at index 2:", arr[2])
print("Slice from index 1 to 3:", arr[1:4])