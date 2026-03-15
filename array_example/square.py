numbers = [2, 4, 6, 8]

def square_numbers(arr):
    squares = []
    
    for n in arr:
        squares.append(n * n)
        
    return squares

result = square_numbers(numbers)

print(result)