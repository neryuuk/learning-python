# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
txtCal = calendar.TextCalendar(calendar.MONDAY)
print(txtCal.formatmonth(2023, 4))

# TODO: create an HTML formatted calendar
htmlCal = calendar.HTMLCalendar(calendar.SUNDAY)
print(htmlCal.formatmonth(2023, 4))

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for day in txtCal.itermonthdays(2023, 4):
    print(day)

# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for month in range(1, 13):
    cal = calendar.monthcalendar(2023, month)
    weekone, weektwo = cal[0], cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print(calendar.month_name[month], meetday)
