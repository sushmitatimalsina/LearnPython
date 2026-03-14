# sales = [1200, 1500, 900, 2000, 1700]

# print(sales)
# print(sales[0])   # first value
# print(sales[2])  
#  # third value

# for s in sales:
#     print(s)

# def calculate_total(sales):
#     total = sum(sales)
#     return total

# sales = [1200, 1500, 900, 2000]

# result = calculate_total(sales)

# print("Total Sales:", result)

def calculate_revenue(prices, quantities):
    revenues = []

    for i in range(len(prices)):
        revenues.append(prices[i] * quantities[i])

    return revenues


prices = [100, 200, 150]
quantities = [2, 3, 4]

result = calculate_revenue(prices, quantities)

print("Revenue per product:", result)