import sqlite3
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

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
      
print(distances)