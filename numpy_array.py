import pandas as pd
import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)