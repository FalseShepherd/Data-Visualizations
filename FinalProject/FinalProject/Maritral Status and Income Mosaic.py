import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

df = pd.read_csv('removedNulls.csv')

print(df["marital-status"].unique())

df = df.replace(' Married-spouse-absent',' Separated', regex=True)
df = df.replace(' Married-AF-spouse',' Separated', regex=True)
mosaic(df, ["marital-status", "income"])
plt.title("Marital Status and Income")
plt.show()