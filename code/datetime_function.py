import datetime
from datetime import date, time

# dir or help commands it is possible to know the available functions
print(dir(datetime))

from datetime import datetime

now = datetime.now()
print(now)
day = now.day
print(day)
month = now.month
year = now.year
print(month)
print(day)

print(f"{now.strftime('%A')} {day} {now.strftime('%B')} {year}")

# number of seconds since the jan 1 1970
timestamp = now.timestamp()
print(timestamp)

print(f"{now.day}/{now.month}/{now.year}, {now.hour}:{now.minute}")


new_year = datetime(2026, 1, 1)
print(new_year)

#  formatting used strftime
# datetime -> string
current_time = now.strftime("%H:%M:%S")
print(current_time)

# strptime string -> datetime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
print(type(date_object))

today = date(2026, 1, 25)
print(today)
print(type(today))

a = time()
print(a)
# time(hour, minute, second, mircosecond)
b = time(10, 30, 50)

# time left for the new year
today = date(
    2026,
    1,
    25
)
new_year = date(
    2027,
    1,
    1
)
time_difference = new_year - today
print(time_difference)

from datetime import timedelta
td1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
td2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
print(td1 - td2)

current_date = datetime.now()
print(current_date)
date_format = current_time = current_date.strftime("%m/%d/%Y, %H:%M:%S")
print(date_format)

today = "5 December, 2019"
today_datetime = datetime.strptime(today, "%d %B, %Y")
print(today_datetime)
print(type(today_datetime))

# difference between the first of jan 1970 and today
first_day = date(
    1970,
    1,
    1
)
today = date(
    2026,
    1,
    25
)

time_difference = today - first_day
print(time_difference)

# datetime module can be used for:
# timeseries analysis
# getting a timestamp of activities in applications
# adding posts on a blog post