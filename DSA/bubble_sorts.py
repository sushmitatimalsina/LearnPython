arr = [9, 6, 8, 2, 33, 55, 4]
n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break        
print(arr)
