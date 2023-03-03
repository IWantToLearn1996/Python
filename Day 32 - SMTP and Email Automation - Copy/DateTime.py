import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.weekday()
time = now.time()
print(f"Now: {now}")

date_of_birth = dt.datetime(year= 1996, month=7, day=12, hour=22, minute=15)
print(f"My Date of Birth: {date_of_birth}")
