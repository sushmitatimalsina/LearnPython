import numpy as np

# # arr = np.array([1,2,3,4,5])
# # print(arr)

# # arr2D = np.array([[1,2],[4,6]])
# # print(arr2D)
# # print(arr2D[0,1])
# # print(arr2D[:, 1] )
# # print(arr2D[1, :]  )

# # print(np.zeros((3, 3)))
# # print(np.ones((2, 4)))

# # print(np.arange(1, 11))

# # arr = np.array([1, 2, 3])
# # print(arr + 5)

# # print(arr * 2)
# # print(arr / 2)

# # a = np.array([1, 2, 3])
# # b = np.array([4, 5, 6])
# # print(a + b)  
# # print(a * b) 

# # arr = np.arange(1, 10)
# # arr.reshape(3, 3)
# # print(arr)

# # print(np.linspace(0, 1, 5))

# # arr = np.array([[1, 2, 3], [4, 5, 6]])
# # # arr.shape
# # print(arr.shape)
# # print(arr.size)


# # print(np.random.rand(3))
# print(np.random.randint(1, 100, 5))

# print(np.random.rand(3, 3))

# arr = np.array([1, 2, 3, 4, 5])

# # Arithmetic operations
# print("Add 5:", arr + 5)
# print("Multiply by 2:", arr * 2)

# # Sum, Mean, Max
# print("Sum:", arr.sum())
# print("Mean:", arr.mean())
# print("Max:", arr.max())


arr = np.array([10, 20, 30, 40, 50])

# Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slice
print("Elements 1 to 3:", arr[1:4])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access row
print("First row:", matrix[0])

# Access column
print("Second column:", matrix[:, 1])

# Element-wise operations
print("Multiply by 2:\n", matrix * 2)

# Random integers from 0 to 9
rand_int = np.random.randint(0, 10, size=(3, 3))
print("Random Integers:\n", rand_int)

# Random floats between 0 and 1
rand_float = np.random.rand(3, 3)
print("Random Floats:\n", rand_float)

import numpy as np

arr = np.arange(12)  # array from 0 to 11
print("Original array:", arr)

# Reshape to 3x4
reshaped = arr.reshape(3, 4)
print("Reshaped array (3x4):\n", reshaped)

# Flatten back
flattened = reshaped.flatten()
print("Flattened array:", flattened)

