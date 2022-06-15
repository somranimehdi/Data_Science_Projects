#!/usr/bin/python
import sys

totalSteps = 0
totalDistance = 0
oldId = None


for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 3:
        continue

    thisId, thatdaySteps, thatdayDistance = data_mapped

    if oldId and oldId != thisId:
        print (oldId, ",", totalSteps,",",totalDistance)
        oldId = thisId;
        totalSteps = 0
        totalDistance = 0
        

    oldId = thisId
    totalSteps += float(thatdaySteps)
    totalDistance+= float(thatdayDistance)

if oldId != None:
    print (oldId, ",", totalSteps,",",totalDistance)
