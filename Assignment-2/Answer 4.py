import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute(
  "SELECT AttractionID, Name FROM attraction WHERE Category LIKE '%Kiddie Rides%'"
)
kiddieRides = c.fetchall()

stats = []

maxPeople = 0

for ride in kiddieRides:
  c.execute(
    "SELECT visitorID, attraction FROM checkin WHERE checkin.attraction = {0}".
    format(ride[0]))
  num = len(c.fetchall())

  stats.append([ride[1], num])

printList = []

for item in stats:
  printList.append(item[1])

print(printList)

rideStats = pd.DataFrame.from_records(stats, columns=["ride", "visits"])

plt.xlabel("visits")
plt.title("Kiddie Ride Box Plot")

plt.boxplot(rideStats["visits"])

plt.show()
