# Import the libraries that will assist in computation
# Pysal contains functions that perform Spatial Autocorrelation computation.
# numpy assists pysal with matrix handling functions and operations.
import libpysal
import numpy as np
import pandas as pd

# Load the income data set from pysal's examples.
income_table = pd.read_csv(libpysal.examples.get_path('usjoin.csv'))

# Select the single column of interest from the dataset.
y = np.array(income_table['2009'])

# Load the Rook continuity matrix for use in Moran's I computation.
w = pd.read_csv(libpysal.examples.get_path('stl.gal'))

# Compute Moran's I for the data.
mi = libpysal.Moran(y, w,two_tailed=False)

# Report that value of Moran's I
print (mi.I)