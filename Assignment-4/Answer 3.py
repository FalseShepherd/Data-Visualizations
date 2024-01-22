import sqlite3
# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("SELECT visitorID, sequence FROM sequences")

visits = []
time = []
for i in range(576):
  visits.append(0)
  time.append(i * 5)

for sequence in c.fetchall():
  rides = sequence[1].split('-')
  for i in range(len(rides)):
    if (rides[i] == '8'):
      visits[i] += 1

stats = {'time': time, 'visits': visits}
df = pd.DataFrame(stats, columns=["time", "visits"])

#find 50 item moving average
window = 50
average_data = []
# weights = []

# for ind in range(len(df["visits"]) - window + 1):
#   average_data.append(np.mean(df["visits"][ind:ind + window]))

# for ind in range(window - 1):
#   average_data.insert(0, np.nan)
average_data = df['visits'].ewm(span=50, adjust=True).mean()
# , columns = ["time", "visits"]
plt.figure().set_figwidth(10)

plt.xlabel("Time (Minutes)")
plt.ylabel("Atmosfear Visits")
# One Standard Deviation

# plt.xticks(np.arange(min(df["time"]), max(df["time"]) + 1, 3000.0))

plt.plot(df["time"], df["visits"])
plt.plot(df["time"], average_data)
plt.show()
