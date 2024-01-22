import pandas as pd
import matplotlib.pyplot as plt

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
                # If counting total respondants
                ratios[column][entry] = num
                # If displaying income percentages
                # ratios[column][entry] = num/len(df[(df[column]==entry)])
            else:
                ratios[column][entry] = 0

myKeys = list(ratios["age"].keys())
myKeys.sort()
ratios["age"] = {i: ratios["age"][i] for i in myKeys}

plt.title("Age and Income >50K")
plt.bar(ratios["age"].keys(),ratios["age"].values())
# If counting total respondants
plt.ylabel("Earn >50K(Count)")
# If displaying income percentages
# plt.ylabel("Earn >50K(Percentage)")
plt.show()
