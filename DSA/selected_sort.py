arr = [7, 11, 9, 12, 3]
n = len(arr)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("sorted value is ", arr)


my_array = list(map(int, input("enter your number :") . split() ) )
a = print( my_array)
b = my_array

m = len(b)

for h in range(m-1):
    min = h
    for k in range(h + 1, m):
        if b[k] < b[min]:
            min = k
    b[h], b[min] = b[min], b[h]
print(b)          




