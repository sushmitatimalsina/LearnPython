import pandas as pd
# Create a small example DataFrame
df2 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['x', 'y'])

print("\nOriginal DataFrame:\n", df2)

# Stack: moves columns to row level
stacked = df2.stack()
print("\nAfter Stack:\n", stacked)

unstacked = stacked.unstack()
print("\nAfter Unstack:\n", unstacked)