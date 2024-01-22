import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute(
  "SELECT AttractionID, Name FROM attraction WHERE Category LIKE '%food%'")
stalls = c.fetchall()

stats = []

maxPeople = 0

for stall in stalls:
  c.execute(
    "SELECT visitorID, attraction FROM checkin WHERE checkin.attraction = {0}".
    format(stall[0]))
  num = len(c.fetchall())

  stats.append([stall[1], num])

print(stats)
stallStats = pd.DataFrame.from_records(stats, columns=['Food Stall', 'visits'])

plt.bar(range(len(stallStats['Food Stall'])), stallStats['visits'])
plt.xticks(range(len(stallStats['Food Stall'])),
           stallStats['Food Stall'],
           rotation='vertical')
plt.show()