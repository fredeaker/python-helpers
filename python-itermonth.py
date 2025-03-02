# https://docs.python.org/3/library/calendar.html
import calendar
from datetime import date

firstweekday = calendar.SUNDAY
month = calendar.JANUARY
year = date.today().year
cal = calendar.Calendar(calendar.SUNDAY)

# itermonth* test

# itermonthdates(year, month)
# Return an iterator for the month month (1–12) in the year year.
# This iterator will return all days (as datetime.date objects) for the month
# and all days before the start of the month or after the end of the month that
# are required to get a complete week.

print('# itermonthdates')

iter_itermonthdates = cal.itermonthdates(year, month)

for date in iter_itermonthdates:
    print(date)

# itermonthdays(year, month)
# Return an iterator for the month month in the year year similar to itermonthdates(),
# but not restricted by the datetime.date range. Days returned will simply be
# day of the month numbers. For the days outside of the specified month,
# the day number is 0.

print('# itermonthdays')

iter_itermonthdays = cal.itermonthdays(year, month)

for day in iter_itermonthdays:
    print(day)

# itermonthdays2(year, month)
# Return an iterator for the month month in the year year similar to itermonthdates(),
# but not restricted by the datetime.date range. Days returned will be tuples
# consisting of a day of the month number and a week day number.

print('# itermonthdays2')

iter_itermonthdays2 = cal.itermonthdays2(year, month)

for day2 in iter_itermonthdays2:
    print(day2)

# itermonthdays3(year, month)
# Return an iterator for the month month in the year year similar to itermonthdates(),
# but not restricted by the datetime.date range. Days returned will be tuples
# consisting of a year, a month and a day of the month numbers.

print('# itermonthdays3')

iter_itermonthdays3 = cal.itermonthdays3(year, month)

for day3 in iter_itermonthdays3:
    print(day3)

# itermonthdays4(year, month)
# Return an iterator for the month month in the year year similar to itermonthdates(),
# but not restricted by the datetime.date range. Days returned will be tuples
# consisting of a year, a month, a day of the month, and a day of the week numbers.

print('# itermonthdays4')

iter_itermonthdays4 = cal.itermonthdays4(year, month)

for day4 in iter_itermonthdays4:
    print(day4)