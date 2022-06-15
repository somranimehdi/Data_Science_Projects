import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 5:
        fit_id, date, day, TotalSteps, TotalDistance = data
        print ("{0},{1},{2}".format(fit_id, TotalSteps,TotalDistance))
