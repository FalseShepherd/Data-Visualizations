import pandas as pd
import matplotlib.pyplot as plt

#read all column names
f1 = open("adult.names", "r")
lineList = f1.readlines()
headers = []

for line in lineList:
  if ":" in line:
    headers.append(line.split(":")[0])

headers = headers[15:]
headers.append("income")

print(headers)
f2 = open("adult.data", "r")
dataString = f2.readlines()
dataTable = []

for line in dataString:
  lines = line.split(",")
  dataTable.append(lines)


df = pd.DataFrame(dataTable, columns=headers)
df = df.replace('\n','', regex=True)

parsedList = []

for index, row in df.iterrows():
  found = False
  for col in headers:
    if row[col] is not None:
      if (str(row[col]) in ' ?'):
        found = True
    else:
      found = True
  if not found:
    parsedList.append(row)


parsedDf = pd.DataFrame(parsedList, columns=headers)

parsedDf.to_csv("removedNulls.csv")

