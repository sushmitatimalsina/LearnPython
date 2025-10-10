import pandas as pd

customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105, 106],
    'customer_name': ['Sita', 'Gita', 'Hari', 'Rita', 'Nabin', None],
    'city': ['Kathmandu', 'Pokhara', 'Lalitpur', None, 'Biratnagar', 'Pokhara'],
    'age': [25, 30, None, 45, 28, 35]
})


sales = pd.DataFrame({
    'order_id': [201, 202, 203, 204, 205, 206],
    'customer_id': [101, 102, 103, 107, 105, 102],
    'product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Headphones', 'Laptop'],
    'amount': [85000, None, 45000, 90000, 7000, 88000],
    'order_date': ['2024-02-10', '2024-03-12', '2024-03-14', '2024-04-01', '2024-05-15', '2024-06-10']
})

customers[ 'customer_name'].fillna('Unknown', inplace = True)
print(customers)

customers['city'].fillna('Not Provided', inplace=True)
print("After filling city:")
print(customers)

customers['age'].fillna(customers['age'].mean(), inplace=True)
print("After filling mean age:")
print(customers)

sales['order_date'] = pd.to_datetime(sales['order_date'])
print("after conveting order_date to datetime")
print(sales)