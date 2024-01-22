import sqlite3

con = sqlite3.connect("dinofunworld.db")
cur = con.cursor()

cur.execute("SELECT * FROM attraction WHERE Category LIKE '%ride%'")

attractions = []

for ride in cur.fetchall():
  cur.execute("SELECT duration FROM checkin WHERE duration IS NOT NULL and attraction=" + str(ride[1]))
  rideDuration =0
  count = 0
  for j in cur.fetchall():
    try:
      h, m, s = j[0].split(':')
      rideDuration += int(h) * 3600 + int(m) * 60 + int(s)
      count += 1
    except (ValueError) as e:
      pass 
  attractions.append([ride[2],count, rideDuration/count])

#PROFESSOR's ALGORITHM ie. naive check against all and see if dominated. 
skyline = []

for attraction1 in attractions: 
  dominated = False
  for attraction2 in attractions: 
    if(attraction2[1] > attraction1[1] and attraction2[2] < attraction1[2]): 
      dominated = True
  if(not dominated):
    skyline.append(attraction1)

print(skyline)

# ALTERNATIVE ALGORITHM sort on 1 dimension and only check second dimension to verify whether item is a skyline (produces same answer in different order)
# def numVisitors(rideInfo):
#   return rideInfo[1]

# #Sort the list in order of greatest -> least visitors.
# attractions.sort(key=numVisitors, reverse=True)

# #The first item has most visitors and so is immediately included in the skyline.
# skyline = [attractions[0]]

# #Check through all the rides and compare them to the rides in skyline. If any of them have a shorter visit time than all current skyline items add it. Since the greatest visitors are added first, no need to check that.
# for ride in attractions:
#   leastTime = True
#   for optimalRide in skyline:
#     if (ride[2] >= optimalRide[2]):
#       leastTime = False
#   if (leastTime):
#     skyline.append(ride)

# . 
# print(skyline)
