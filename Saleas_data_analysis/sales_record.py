import numpy as np

sales_data = np.array([
    [101, 20, 50],   
    [102, 40, 30],
    [103, 15, 80],
    [101, 10, 50],
    [102, 60, 30],

])

revenue = sales_data[:, 1] * sales_data[:, 2]
total_revenue = revenue.sum()
print("Total Revenue:", total_revenue)