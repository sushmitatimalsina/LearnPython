import pandas as pd 

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 80, 85],
    'English': [88, 82, 89]
})

print("Original (Wide Format):\n", df, "\n")

melted = pd.melt(df, id_vars=['Name'], 
                 var_name='Subject', 
                 value_name='Score')
print("After Melt (Long Format):\n", melted)

# Pivot: convert from long back to wide
pivoted = melted.pivot(index='Name', columns='Subject', values='Score')
print("\nAfter Pivot (Back to Wide Format):\n", pivoted)