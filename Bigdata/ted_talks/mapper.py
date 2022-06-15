import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 6:
        id_x, auth, day, views, likes,something = data
        print ("{0},{1},{2}".format(auth, views,likes))
