"""Q4: Write a python program to take date (only date) and number of years to add in that
date from a file. Display the updated date on console after adding those days
Sample Content of File
> 29 August 2024
> 10

 (File Name: 29Aug_Q4.txt)
 """
from datetime import datetime, timedelta

with open("29Aug_Q4.txt", "r+") as fil:
    x = fil.readlines()
    if len(x) != 2:
        print("wrong number of lines in input")
        exit(-1)

    try:
        parsed_date = datetime.strptime(x[0], '%d %B %Y\n')
    except ValueError as e:
        print(f"invalid date: {e}")
        exit(-1)

    try:
        parsed_days = int(x[1])
    except ValueError as e:
        print(f"invalid days to add: {e}")
        exit(-1)

print(parsed_date+timedelta(days=parsed_days))

