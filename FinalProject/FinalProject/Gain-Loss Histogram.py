import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('removedNulls.csv')

count = []

for index, row in df.iterrows():
    count.append(row["capital-gain"] - row["capital-loss"])

df["Net-Gain-Loss"] = count

plt.title("Net Gains & Losses and Income >50K")
plt.axis([-5000, 10000, 0, 9000])
plt.hist(count, bins=[-4000, -3000, -2000,-1000, 0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
plt.xlabel("Net Capital Gains & Losses")
plt.ylabel("Earn >50K")
plt.show()
