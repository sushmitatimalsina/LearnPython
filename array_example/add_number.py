numbers = [5, 10, 15, 20]

def add_numbers(arr):
    total = 0
    for n in arr:
        total = total + n
    return total

result = add_numbers(numbers)

print("Total:", result)