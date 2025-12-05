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


# arr = np.array([10, 20, 30, 40, 50])

# # Access elements
# print("First element:", arr[0])
# print("Last element:", arr[-1])

# # Slice
# print("Elements 1 to 3:", arr[1:4])

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Access row
# print("First row:", matrix[0])

# # Access column
# print("Second column:", matrix[:, 1])

# # Element-wise operations
# print("Multiply by 2:\n", matrix * 2)

# # Random integers from 0 to 9
# rand_int = np.random.randint(0, 10, size=(3, 3))
# print("Random Integers:\n", rand_int)

# # Random floats between 0 and 1
# rand_float = np.random.rand(3, 3)
# print("Random Floats:\n", rand_float)

# import numpy as np

# arr = np.arange(12)  # array from 0 to 11
# print("Original array:", arr)

# # Reshape to 3x4
# reshaped = arr.reshape(3, 4)
# print("Reshaped array (3x4):\n", reshaped)

# # Flatten back
# flattened = reshaped.flatten()
# print("Flattened array:", flattened)


# arr = np.array([10, 15, 20, 25, 30])

# # Filter values greater than 20
# filtered = arr[arr > 20]
# print("Values greater than 20:", filtered)

# # Boolean mask
# mask = arr % 20 == 0
# print("Mask for values divisible by 20:", mask)
# print("Filtered values:", arr[mask])



# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Sum of all elements
# print("Total sum:", matrix.sum())

# # Sum along rows (axis=1)
# print("Sum of each row:", matrix.sum(axis=1))

# # Sum along columns (axis=0)
# print("Sum of each column:", matrix.sum(axis=0))

# # Mean along columns
# print("Mean of each column:", matrix.mean(axis=0))

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Horizontal stack
# h_stack = np.hstack((a, b))
# print("Horizontal Stack:", h_stack)

# # Vertical stack
# v_stack = np.vstack((a, b))
# print("Vertical Stack:\n", v_stack)

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# # Matrix multiplication
# C = np.dot(A, B)
# print("Matrix multiplication:\n", C)

# # Element-wise multiplication
# E = A * B
# print("Element-wise multiplication:\n", E)

# # Transpose
# print("Transpose of A:\n", A.T)

data = np.array([10, 20, -1, 30, -1, 40], dtype=float)
missing_mask = data == -1
data[missing_mask] = data[~missing_mask].mean()
print("Data after handling missing values:", data)
