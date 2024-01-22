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
# , columns = ["time", "visits"]
plt.figure().set_figwidth(10)
plt.xlabel("Time (Minutes)")
plt.ylabel("Atmosfear Visits")
# One Standard Deviation
plt.axhline((statistics.mean(visits)) + df["visits"].std(),
            color='red',
            linestyle='dashed')
plt.axhline((statistics.mean(visits)) - df["visits"].std(),
            color='red',
            linestyle='dashed')
# Two Standard Deviation
plt.axhline((statistics.mean(visits)) + 2 * df["visits"].std(),
            color='green',
            linestyle='dashed')
plt.axhline((statistics.mean(visits)) - 2 * df["visits"].std(),
            color='green',
            linestyle='dashed')
# Mean
plt.axhline((statistics.mean(visits)), color='blue')

print(visits)
print(statistics.mean(visits))
print(df["visits"].std())

plt.plot(df["time"], df["visits"])
plt.show()
