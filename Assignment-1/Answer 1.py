import sqlite3
con = sqlite3.connect("dinofunworld.db")
cur = con.cursor()

cur.execute("SELECT * FROM attraction")

greatest = []
numPeople = 0

for ride in cur.fetchall():
  cur.execute("SELECT visitorID, attraction FROM checkin WHERE checkin.attraction = {0}".format(ride[1]))
  num = len(cur.fetchall())
  if (num > numPeople): 
    numPeople = num
    greatest = ride[2]

print (str(greatest))

