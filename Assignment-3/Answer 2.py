import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute(
  "SELECT DISTINCT AttractionID, Name from attraction WHERE Category LIKE '%ride%'"
)
rides = []
for item in c.fetchall():
  rides.append((item[0], item[1]))

c.execute("SELECT sequence FROM sequences")
sequences = c.fetchall()
initData = []

for sequence in sequences:
  list = sequence[0].split('-')
  initData.append(list)

finalData = {}
maxList = []
minList = []
avgList = []
max = 0
min = 999999999999
total = 0
count = 0

for rideNum in rides:
  for col in range(576):
    for row in range(len(initData)):
      if (initData[row][col] == str(rideNum[0])):
        count += 1
    if (count < min and count != 0):
      min = count
    if (count > max):
      max = count
    total += count
    count = 0
  finalData[rideNum[0]] = {
    'name': rideNum[1],
    'min': min,
    'max': max,
    'avg': total / 576
  }
  maxList.append(max)
  minList.append(min)
  avgList.append(total / 576)
  max, total, count = 0, 0, 0
  min = 999999999999

data = pd.DataFrame([[i['name'], i['min'], i['avg'], i['max']]
                     for i in finalData.values()],
                    columns=['Ride', 'Minimum', 'Average', 'Maximum'])

pd.plotting.parallel_coordinates(data, 'Ride')
plt.title("Min/Max/Avg Attendance at 'Rides'")
plt.gca().get_legend().remove()
plt.show()

print(finalData)
