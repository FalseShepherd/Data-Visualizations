
# # print(checkins)
# timeList = []

# for checkin in checkins: 
#   dt = datetime.strptime(checkin[0], '%Y-%m-%d %H:%M:%S')
#   timeList.append(dt)

# #sort the TimeList so that earlier datesTimes are first.
# timeList.sort()

# #Only look at first 16 hours of data. 
# for i in range(len(timeList)):
#   if(abs((timeList[i] - timeList[0]).total_seconds()) > timedelta(hours=16).total_seconds()):
#     timeList = timeList[0:i]
#     break
    
# current = 0
# i = 0
# group =0

# #add items to the groupedCheckins dictionary
# #groups advance in 5 minute intervals. 
# #if the absolute difference between the times > 5, inner loop breaks and advances to next group. 
# groupedCheckins = {}
# while (i < len(timeList)):
#   groupedCheckins[group] =  []
#   while(i < len(timeList) and abs((timeList[i]-timeList[current]).total_seconds())<= timedelta(minutes=5).total_seconds()):
#     groupedCheckins[group].append(timeList[i])
#     i=i+1
#   current=i
#   group+=5

# #count the number of visits in each 5 minute interval. 
# stats = {}
# for key in groupedCheckins.keys(): 
#   stats[key] = len(groupedCheckins[key])

# #format it in the tuple format asked for by the question. 
# printList = []
# for key in stats.keys(): 
#   printList.append([key, stats[key]])
