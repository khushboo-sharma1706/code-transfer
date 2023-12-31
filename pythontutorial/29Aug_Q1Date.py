"""Q1: Write a program to write current date and time in UTC timezone and UTC+1
timezone in a file called "current_data_time.txt" in write mode. (Handle all exception)"""


from datetime import date, datetime, timedelta

current_datetime = datetime.utcnow()


with open("current_data_time.txt", "w") as f:
    f.write(f"UTC+1 timezone : {(current_datetime + timedelta(hours=1)).strftime('%d %B %Y %H:%M:%S')}\n")
    f.write(f"UTC timezone :{current_datetime.strftime('%d %B %Y %H:%M:%S')}")
