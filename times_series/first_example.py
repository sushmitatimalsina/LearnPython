import pandas as pd

data = {
    'date': ['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-05'],
    'sales': [200, 220, 250, 230, 210]
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)
weekly_sales = df.resample('W').sum()
print("Weekly Sales:\n", weekly_sales)

df['day_of_week'] = df.index.day_name()
df['month'] = df.index.month
print("\nData with day and month:\n", df)