numbers = [12, 45, 7, 30, 25]

def find_largest(arr):
    largest = arr[0]
    
    for n in arr:
        if n > largest:
            largest = n
            
    return largest

print("Largest number:", find_largest(numbers))