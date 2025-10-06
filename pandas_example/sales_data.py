import pandas as pd

data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Keyboard", "Laptop"],
    "region": ["East", "East", "East", "West", "West", "West", "East"],
    "units_sold": [10, 50, 30, 20, 60, 40, 15],
    "price_per_unit": [1000, 20, 50, 1000, 20, 50, 1000]
}

df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

# calculate total sales for each row 
df["total_sales"] = df["units_sold"] * df["price_per_unit"]
print("\nDataFrame with Total Sales:")
print(df)

# total sales by product
total_sales_by_product = df.groupby("product")["total_sales"].sum().reset_index()
print("\nTotal Sales by Product:")
print(total_sales_by_product)

region_avg_sales = df.groupby("region")["total_sales"].mean().reset_index()
print("\nAverage Sales by Region:")
print(region_avg_sales)

# highest selling product
highest_selling_product = df.groupby("product")["units_sold"].sum().idxmax()
print(f"\nHighest Selling Product: {highest_selling_product}")



#  Sort products by total sales descending
sorted_sales = total_sales_by_product.sort_values(by="total_sales", ascending=False)
print("\nProducts sorted by total sales:")
print(sorted_sales)