#Q3: Write a program to print yesterday, today, tomorrow on console.

from datetime import date, timedelta

today = date.today()
print(today)
print(today + timedelta(days=-1))
print(today + timedelta(days=1))
