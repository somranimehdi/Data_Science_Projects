import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 10:
        Country,Other_names,code,Population,Continent,Total_Cases,Total_Deaths,Tot_Cases_per_onemel,Tot_Deaths_per_onemel,Death_percentage = data
        print ("{0},{1}".format(Continent, Total_Deaths))
        


