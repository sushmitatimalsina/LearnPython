import pandas as pd
import numpy as np

arr = np.random.randint(1, 10, size=(4, 3))
df = pd.DataFrame(arr, columns=["A", "B", "C"])
print("DataFrame created from NumPy array:")
print(df)