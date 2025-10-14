import pandas as pd

# Sample data
data = {
    'Region': ['East', 'West', 'East', 'North', 'West', 'North'],
    'Salesperson': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Sales': [200, 150, 300, 400, 250, 350]
}

df = pd.DataFrame(data)

# Aggregate total sales by region
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

print(region_sales)