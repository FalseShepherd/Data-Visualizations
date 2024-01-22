import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

# # c.execute("SELECT DISTINCT AttractionID, Name from attraction WHERE Category LIKE '%ride%'")
# rides = []
# for item in c.fetchall():
#   rides.append((item[0], item[1]))

finalData = {
  1: {
    'name': 'Wrightiraptor Mountain',
    'min': 1,
    'max': 158,
    'avg': 52.75
  },
  2: {
    'name': 'Galactosaurus Rage',
    'min': 1,
    'max': 261,
    'avg': 56.63715277777778
  },
  3: {
    'name': 'Auvilotops Express',
    'min': 1,
    'max': 640,
    'avg': 118.97916666666667
  },
  4: {
    'name': 'TerrorSaur',
    'min': 2,
    'max': 424,
    'avg': 248.09375
  },
  5: {
    'name': 'Wendisaurus Chase',
    'min': 5,
    'max': 491,
    'avg': 233.6875
  },
  6: {
    'name': 'Keimosaurus Big Spin',
    'min': 2,
    'max': 206,
    'avg': 64.39756944444444
  },
  7: {
    'name': 'Firefall',
    'min': 1,
    'max': 576,
    'avg': 233.46875
  },
  8: {
    'name': 'Atmosfear',
    'min': 5,
    'max': 335,
    'avg': 126.359375
  },
  9: {
    'name': 'North Line',
    'min': 1,
    'max': 166,
    'avg': 45.06944444444444
  },
  10: {
    'name': 'Jeredactyl Jump',
    'min': 1,
    'max': 112,
    'avg': 21.66840277777778
  },
  11: {
    'name': 'Sauroma Bumpers',
    'min': 1,
    'max': 148,
    'avg': 23.866319444444443
  },
  12: {
    'name': 'Flying TyrAndrienkos',
    'min': 1,
    'max': 98,
    'avg': 19.76215277777778
  },
  13: {
    'name': 'Cyndisaurus Asteroid',
    'min': 1,
    'max': 72,
    'avg': 12.947916666666666
  },
  14: {
    'name': 'Beelzebufo',
    'min': 1,
    'max': 93,
    'avg': 13.869791666666666
  },
  15: {
    'name': 'Enchanted Toadstools',
    'min': 1,
    'max': 77,
    'avg': 12.864583333333334
  },
  16: {
    'name': 'Stegocycles',
    'min': 1,
    'max': 76,
    'avg': 13.276041666666666
  },
  17: {
    'name': 'Blue Iguanodon',
    'min': 1,
    'max': 73,
    'avg': 13.18923611111111
  },
  18: {
    'name': 'Wild Jungle Cruise',
    'min': 1,
    'max': 90,
    'avg': 14.883680555555555
  },
  19: {
    'name': 'Stone Cups',
    'min': 1,
    'max': 70,
    'avg': 12.34375
  },
  20: {
    'name': 'Scholtz Express',
    'min': 1,
    'max': 185,
    'avg': 66.12152777777777
  },
  21: {
    'name': 'Paleocarrie Carousel',
    'min': 1,
    'max': 99,
    'avg': 28.932291666666668
  },
  22: {
    'name': 'Jurassic Road',
    'min': 1,
    'max': 86,
    'avg': 20.395833333333332
  },
  23: {
    'name': 'Rhynasaurus Rampage',
    'min': 1,
    'max': 76,
    'avg': 16.635416666666668
  },
  24: {
    'name': "Kauf's Lost Canyon Escape",
    'min': 1,
    'max': 133,
    'avg': 22.413194444444443
  },
  25: {
    'name': 'Maiasaur Madness',
    'min': 1,
    'max': 91,
    'avg': 21.291666666666668
  },
  26: {
    'name': 'Kristanodon Kaper',
    'min': 1,
    'max': 138,
    'avg': 30.34027777777778
  },
  27: {
    'name': 'Squidosaur',
    'min': 1,
    'max': 109,
    'avg': 19.65972222222222
  },
  28: {
    'name': 'Eberlesaurus Roundup',
    'min': 1,
    'max': 76,
    'avg': 17.211805555555557
  },
  29: {
    'name': 'Dykesadactyl Thrill',
    'min': 1,
    'max': 62,
    'avg': 14.993055555555555
  },
  30: {
    'name': 'Ichthyoroberts Rapids',
    'min': 1,
    'max': 404,
    'avg': 191.14583333333334
  },
  31: {
    'name': 'Raptor Race',
    'min': 1,
    'max': 94,
    'avg': 19.4375
  },
  81: {
    'name': 'Flight of the Swingodon',
    'min': 3,
    'max': 534,
    'avg': 253.93055555555554
  }
}

data = pd.DataFrame([[i['min'], i['avg'], i['max']] for i in finalData.values()], columns=['Minimum', 'Average', 'Maximum'])

pd.plotting.scatter_matrix(data)
plt.title("Min/Max/Avg Attendance at 'Rides'")
plt.show()
# plt.title("Min/Max/Avg Attendance at 'Rides'")
# plt.xlabel("Rides", labelpad=7)
# chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')
# plt.gca().get_legend().remove()
# c.execute(
#   "SELECT sequence FROM sequences"
# )
# sequences = c.fetchall()
# initData= []

# for sequence in sequences:
#   list = sequence[0].split('-')
#   initData.append(list)

# finalData = {}
# maxList = []
# minList = []
# avgList = []
# max = 0
# min = 999999999999
# total = 0
# count = 0

# for rideNum in rides:
#   for col in range(576):
#     for row in range(len(initData)):
#       if(initData[row][col] == str(rideNum[0])):
#         count += 1
#     if(count < min and count != 0):
#       min = count
#     if(count > max):
#       max =  count
#     total += count
#     count = 0
#   finalData[rideNum[0]] = {'name':rideNum[1], 'min': min, 'max': max, 'avg' : total/576 }
#   maxList.append(max)
#   minList.append(min)
#   avgList.append(total/576)
#   max, total, count = 0, 0, 0
#   min = 999999999999

print(finalData)

# parallel_coordinates(finalData, "Max/Min/Avg")
