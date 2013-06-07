import numpy as np
import pandas as pd
data = np.load('table.npy')

print(data)
data = data.byteswap().newbyteorder()
print(data)
df = pd.DataFrame.from_records(data)
print(df)
df = df.set_index(['ROI', 'Solution'])
print(df)
print(df[['nfev','numpoints']])