#!/usr/bin/python

import sys

salesTotal = 0
numberOfSales = 0

oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thiskey, currentSale = data_mapped

    if oldKey and oldKey != thiskey:
        print (oldKey, "\t", salesTotal)
        oldKey = thiskey;
        salesTotal = 0
        

    oldKey = thiskey
    salesTotal += float(currentSale)
    

if oldKey != None:
    print (oldKey, "\t", salesTotal)