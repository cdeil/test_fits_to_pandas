import pandas as pd
table = pd.read_csv('table.csv')
table = table.set_index(['ROI', 'Solution'])
print(table.head())
print(table.xs('HESS_J1023m575'))
print(table[['nfev', 'statname']])
