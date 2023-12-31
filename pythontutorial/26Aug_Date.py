import time
from datetime import date, datetime, timedelta

# Get Current Date and Time
print(datetime.now())
print(datetime.today())

# Get Current Date
print(date.today())

# Create a new Date
print(date(2000, 6, 17))

# Epoch Date -> Numbers of Second from Jan 1 1970 at UTC/GMT
print(datetime.now())
print(int(time.time()))  # Get Current Epoch Value
print(datetime.fromtimestamp(1693061368))  # Get Date Time from Epoch Value

# Print Current Year, Month and Date
today = date.today()
print(f"{today}, year: {today.year}, month: {today.month}, date: {today.day}")

# Print Hour, Minute, Second and Microsecond
now = datetime.now()
print(
    f"{now}, year: {now.year}, month: {now.month}, date: {now.day}, hour: {now.hour}, minute: {now.minute}, second: {now.second}, ms: {now.microsecond}")

# Print Date in Form "26 August 2023"
print(now.strftime("%d %B %Y"))
print(datetime.utcnow().strftime("%d %b %Y %p %Z %j"))

# TimeDelta
t1 = datetime(year=2018, month=7, day=12, hour=20, minute=40)
t2 = datetime(year=2017, month=12, day=23)

print(t1-t2)

print(datetime.now() + timedelta(days=10))
print(datetime.now() + timedelta(hours=-10))
print("------")
print(datetime.utcnow())
print(datetime.now())

current_datetime = datetime.now()
print((current_datetime + timedelta(hours=-5, minutes=-30)).strftime("%d %B %Y %H:%M:%S"))
# 26 August 2023

# Convert String to Datetime
input="26 August 2023 15:50:50"
print(datetime.strptime(input, "%d %B %Y %H:%M:%S"))
print(datetime.utcnow())