numbers = [3, 6, 9, 12, 15, 18]

def get_even_numbers(arr):
    even = []
    
    for n in arr:
        if n % 2 == 0:
            even.append(n)
            
    return even

result = get_even_numbers(numbers)

print("Even numbers:", result)