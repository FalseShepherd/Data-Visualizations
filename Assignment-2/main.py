import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("SELECT AttractionID, Name FROM attraction WHERE Category LIKE '%Thrill Rides%'")
rides = c.fetchall()

stats = []

for ride in rides: 
  c.execute("SELECT visitorID, attraction FROM checkin WHERE checkin.attraction = {0}".format(ride[0]))
  num = len(c.fetchall())
  stats.append([ride[1], num])

visitStats = pd.DataFrame.from_records(stats, columns=['ride', 'visits'])


plt.pie(visitStats['visits'], labels=visitStats['ride'], shadow=False)
plt.show()