import pandas as pd
from astropy.table import Table

def read_fits_as_dataframe(filename, index_columns):
    # This is the way to read the FITS data into a numpy structured array
    # (using astropy.io.fits.getdata didn't work out of the box
    # because it gives a FITSRec)
    table = Table.read(filename)
    data = table._data
    # Fix byte order.
    # See https://github.com/astropy/astropy/issues/1156
    data = data.byteswap().newbyteorder()
    df = pd.DataFrame.from_records(data)
    # Strip whitespace for string columns that will become indices
    for index_column in index_columns:
        df[index_column] = df[index_column].map(str.strip)
    df = df.set_index(index_columns)
    return df

df = read_fits_as_dataframe('table.fits', ['ROI', 'Solution'])
print(df.head())
print(df.xs('HESS_J1023m575'))
print(df[['nfev', 'statname']])
