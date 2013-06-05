import pandas as pd
from astropy.table import Table
astro_table = Table.read('table.fits')
table = pd.DataFrame(astro_table._data)
table = table.set_index(['ROI', 'Solution'])
print(table.head())
#print(table.xs('HESS_J1023m575'))
print(table[['nfev', 'statname']])
