#!/usr/bin/python
import sys

totalDeaths = 0
totalDistance = 0
prevCountry = None


for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue

    thisCountry, deathsPerCountry = data_mapped

    if prevCountry and prevCountry != thisCountry:
        print (prevCountry, ",", totalDeaths)
        prevCountry = thisCountry;
        totalDeaths = 0
        totalDistance = 0
        

    prevCountry = thisCountry
    totalDeaths += float(deathsPerCountry)

if prevCountry != None:
    print (prevCountry, ",", totalDeaths)
