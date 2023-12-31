"""Q5: Write a program to read two dates from a file and append back the difference between
those two dates in the same file. (File Name: 29Aug_Q5.txt)"""

from datetime import datetime, timedelta

with open("29Aug_Q5.txt", "r+") as fil:
    x = fil.readlines()
    print(x)

    if len(x) < 2:
        print("wrong number of lines in input")
        exit(-1)

    try:
        x1 = datetime.strptime(x[0], '%d %B %Y %H:%M:%S\n')
    except ValueError as e:
        print(f"invalid date: {e}")
        exit(-1)
    try:
        x2 = datetime.strptime(x[1], '%d %B %Y %H:%M:%S\n')
    except ValueError as e:
        print(f"invalid date: {e}")
        exit(-1)

    print(x1-x2)
    fil.write(f"\n{x1-x2}")