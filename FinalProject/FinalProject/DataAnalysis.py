import numpy
import scipy
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

df = pd.read_csv('removedNulls.csv')

ratios = {}
print(df.columns)
for column in df.columns:
    ratios[column] = {}


for column in df.columns:
    # print(column + ": " + str(len(df[column].unique())))
    if(str(column) != "fnlwgt" and str(column) != "Unnamed: 0"):
        for entry in df[column].unique():
            num =  len(df[(df[column]==entry) & (df["income"] == " >50K")])
            if(len(df[(df[column]==entry)]) != 0):
                ratios[column][entry] = num/len(df[(df[column]==entry)])
            else:
                ratios[column][entry] = 0

for column in ratios.keys():
    sorted_tuples = sorted(ratios[column].items(), key=lambda x: x[1], reverse = True)
    converted_dict = dict(sorted_tuples)
    ratios[column] = converted_dict



plt.bar(ratios["education"].keys(),ratios["education"].values() )
plt.xticks(range(len(ratios["education"].keys())),ratios["education"].keys(),  rotation='vertical')
plt.ylabel("Earn >50K (Percentage)")
plt.show()
