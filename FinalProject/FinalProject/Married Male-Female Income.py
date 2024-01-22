import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('removedNulls.csv')

incomes = {}
Men = len(df[(df["sex"] == " Male") & (df["marital-status"] == " Married-civ-spouse") & (df["income"] == " >50K")])
incomes["Married Men"] = round(Men/len(df[(df["sex"] == " Male") & (df["marital-status"] == " Married-civ-spouse")]) * 100, 5)

Women = len(df[(df["sex"] == " Female") & (df["marital-status"] == " Married-civ-spouse") & (df["income"] == " >50K")])
incomes["Married Women"] = round(Women/len(df[(df["sex"] == " Female") & (df["marital-status"] == " Married-civ-spouse")]) * 100, 5)

Men = len(df[(df["sex"] == " Male") & (df["marital-status"] != " Married-civ-spouse") & (df["income"] == " >50K")])
incomes["Unmarried Men"] = round(Men/len(df[(df["sex"] == " Male") & (df["marital-status"] != " Married-civ-spouse")]) * 100, 5)

Women = len(df[(df["sex"] == " Female") & (df["marital-status"] != " Married-civ-spouse") & (df["income"] == " >50K")])
incomes["Unmarried Women"] = round(Women/len(df[(df["sex"] == " Female") & (df["marital-status"] != " Married-civ-spouse")]) * 100, 5)

print (incomes["Unmarried Men"])
plt.title("Married Men/Women and Income >50K")
plt.bar(incomes.keys(),incomes.values())
plt.ylabel("Earn >50K (Percentage)")
plt.show()