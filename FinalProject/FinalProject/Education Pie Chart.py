import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('removedNulls.csv')

degreeDict = {}
preHSCount = 0
higherEducation = [' Bachelors', ' HS-grad', ' Masters', ' Some-college', ' Assoc-acdm', ' Doctorate', ' Assoc-voc', ' Prof-school']
print(df["education"].unique())
for degree in df["education"].unique():
    if degree not in higherEducation:
        preHSCount += len(df[(df["education"] == degree) & (df["income"] == " >50K")])
    else:
        num = len(df[(df["education"] == degree) & (df["income"] == " >50K")])
        degreeDict[degree] = num

degreeDict["Pre High School"] = preHSCount

plt.title("Percentage of Earners >50K with Degrees")
plt.pie(degreeDict.values(), labels = degreeDict.keys(),  autopct='%1.1f%%', shadow = False )
plt.show()