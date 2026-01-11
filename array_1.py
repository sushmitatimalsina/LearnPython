import array as arr

# # # numbers = [10, 20, 30, 40, 50]
# # # print(numbers[0])

# # # numbers[2] = 35
# # # print(numbers)

# # # for num in numbers:
# # #     print(num)

# # numbers = [10, 20, 30, 40, 50]
# # print(numbers)

# # print(numbers[0])
# # print(numbers[3])  
# # numbers.append(60)
# # print(numbers)
# # numbers.remove(20)
# # print(numbers)


# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# print("1D Array:", arr)

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# print("\n2D Array:\n", matrix)


# print("\nArray + 10:", arr + 10)        
# print("Array * 2:", arr * 2)            
# print("Sum of array:", np.sum(arr))     
# print("Mean of array:", np.mean(arr))  
# print("Max of array:", np.max(arr))     

# print("\nElement at index 2:", arr[2])
# print("Slice from index 1 to 3:", arr[1:4])

numbers =[10,20,30,40,50]

print(numbers)
print(numbers[4])

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


employees = [
    {"id": 1, "name": "Ram", "role": "Analyst"},
    {"id": 2, "name": "Sita", "role": "Engineer"},
    {"id": 3, "name": "Hari", "role": "Manager"}
]

for emp in employees:
    print(emp["name"], "-", emp["role"])
    print("----------------")

order = {
    "order_id": 1001,
    "customer": "Sushmita",
    "items": ["Pen", "Notebook", "Pencil"],
    "total_price": 340
}

print(order["customer"])
print(order["items"])
print(order["items"][0])  
print("---------------------") 


sales = [
    {"order_id": 1, "product": "Pen", "quantity": 10, "price": 5},
    {"order_id": 2, "product": "Notebook", "quantity": 5, "price": 50},
    {"order_id": 3, "product": "Pencil", "quantity": 20, "price": 2}
]

for sale in sales:
    total = sale["quantity"] * sale["price"]
    print(sale["product"], "Total:", total)


