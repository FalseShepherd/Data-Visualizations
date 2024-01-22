import sqlite3
con = sqlite3.connect("dinofunworld.db")
cur = con.cursor()

cur.execute("SELECT * FROM attraction WHERE Category LIKE '%ride%'")

tuples = []

for ride in cur.fetchall():
  cur.execute(
  "SELECT duration FROM checkin WHERE checkin.attraction = {0}"
  .format(ride[1]))
  durations = cur.fetchall()
  totalTime = 0
  for time in durations: 
    if time[0] != None:
      listTime = time[0].split(':')
      totalTime += float(listTime[0]) * 3600 + float(listTime[1])*60 + float(listTime[2])

  avgDuration = totalTime/len(durations)
  tuples.append([ride[1], avgDuration])


def rideTimes(rideTuple):
  return rideTuple[1]

tuples.sort(reverse = True, key = rideTimes)

cur.execute("SELECT * FROM attraction WHERE AttractionID = {0}".format(tuples[1][0]))
secondGreatest = cur.fetchall()

print(secondGreatest[0][2])

