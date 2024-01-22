import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('removedNulls.csv')

count = []

for index, row in df.iterrows():
    count.append(row["capital-gain"] - row["capital-loss"])

df["Net-Gain-Loss"] = count
df["Net-Gain-Loss"]= df["Net-Gain-Loss"].round(decimals=-3)

ratios= {}

for gain_loss in df["Net-Gain-Loss"].unique():
    num = len(df[(df["Net-Gain-Loss"]==gain_loss) & (df["income"] == " >50K")])
    ratios[gain_loss] = (num/len(df[(df["Net-Gain-Loss"]==gain_loss)]))* 100


sorted_tuples = sorted(ratios.items(), key=lambda x: x[0])
ratios = dict(sorted_tuples)

plt.title("Net Gains & Losses and Income >50K")
plt.bar(range(len(ratios)),ratios.values())
plt.xticks(range(len(ratios)),ratios.keys(),  rotation='vertical')
plt.ylabel("Earn >50K (Percentage)")
plt.xlabel("Net Gain/Loss")
plt.show()
