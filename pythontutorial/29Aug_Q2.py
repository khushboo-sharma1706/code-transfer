"""Q2: Write a program to take input of date and time from user in console and parse it
to datetime and then write it back to file "input_date_time.txt" (Handle all exception)"""
from datetime import datetime

while True:
    ci = input("Enter Date and Time: ")
    try:
        parsed_date = datetime.strptime(ci, '%d %B %Y %H:%M:%S')
        break
    except ValueError as e:
        print(f"Invalid Date and Time: {e}")

with open("input_data_time.txt", "w") as f:
    f.write(f"{parsed_date}")