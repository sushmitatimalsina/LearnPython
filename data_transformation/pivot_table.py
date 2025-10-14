import pandas as pd

# Sample data
data = {
    'Region': ['East', 'West', 'East', 'North', 'West', 'North'],
    'Salesperson': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Sales': [200, 150, 300, 400, 250, 350]
}

df = pd.DataFrame(data)

# Pivot table: total sales by region and salesperson
pivot = df.pivot_table(index='Region', columns='Salesperson', values='Sales', fill_value=0)

print(pivot)