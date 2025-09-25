def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
    
numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
print(result)