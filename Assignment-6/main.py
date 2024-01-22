import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

db_filename = 'dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute(
  "SELECT visitorID, sequence FROM sequences WHERE visitorID in (165316, 1835254, 296394, 404385, 448990)"
)
sequences = c.fetchall()
distances = {}
initData= []

for sequence in sequences: 
  list = sequence[1].split('-')
  initData.append([sequence[0], list])

for sequence1 in initData: 
  distances[sequence1[0]] = {}
  for sequence2 in initData: 
    if(sequence1[0] != sequence2[0]):
      distance = 0
      for i in range(576):
        if(sequence1[1][i] != sequence2[1][i]):
          distance += 1
      distances[sequence1[0]][sequence2[0]]= distance

data_table= []
i = 0
j = 0
for key1 in distances.keys():
  data_table.append([])
  for key2 in distances[key1].keys():
    if(i == j):
      data_table[i].append(0) 
    data_table[i].append(distances[key1][key2])
    j+=1
  i+=1
  j = 0

data_table[4].append(0)
mat = np.array(data_table)

dists = squareform(mat)

links = linkage(dists, 'complete')

dendrogram(links, labels=["165316", "1835254", "296394", "404385", "448990"])
plt.xlabel("Visitors")
plt.ylabel("Distances")
plt.title("Vistitor Distance Dendogram")
plt.show()