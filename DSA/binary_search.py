def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1      
numbers = [2, 4, 6, 8, 10, 12, 14] 
target = 10
result = binary_search(numbers, target)
print(result)  

# if target is not present in the list
# return -1

def binary(a, target1):
    left = 0
    right = len(a) - 1
    while left <= right:
        m = (left + right) // 2
        if a[m] == target1:
            return m
        elif a[m] < target1:
            left = m + 1
        else:
            right = m - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target1 = 14
result1 = binary(arr, target1)
print(result1)        