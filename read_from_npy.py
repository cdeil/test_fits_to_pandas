import numpy as np
import pandas as pd
data = np.load('table.npy')
print(data.dtype)
table = pd.DataFrame(data)
table = table.set_index(['ROI', 'Solution'])
print(table.head())
#print(table.xs('HESS_J1023m575'))
print(table[['nfev', 'statname']])
