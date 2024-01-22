import sqlite3
con = sqlite3.connect("dinofunworld.db")
cur = con.cursor()

cur.execute("SELECT * FROM attraction WHERE Category LIKE '%food%'")

min = float('inf')
location = []

for local in cur.fetchall():
  cur.execute("SELECT visitorID, attraction FROM checkin WHERE checkin.attraction = {0}".format(local[1]))
  num = len(cur.fetchall())
  
  if (num < min): 
    min = num
    location = local[2]

print(location)

