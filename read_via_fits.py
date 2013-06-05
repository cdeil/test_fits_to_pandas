import pandas as pd
from astropy.io import fits
data = fits.getdata('table.fits', 1)
table = pd.DataFrame(data)
table = table.set_index(['ROI', 'Solution'])
print(table.head())
#print(table.xs('HESS_J1023m575'))
print(table[['nfev', 'statname']])
