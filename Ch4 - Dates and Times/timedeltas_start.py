from datetime import date, time, datetime, timedelta


# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
print("Today is {}".format(now))

# TODO: print today's date one year from now
print("One year from now will be {}".format(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("In two weeks and 3 days will be {}".format(
    now + timedelta(weeks=2, days=3)
))

# TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print(t.strftime("One week ago it was %A %B %d, %Y"))

# How many days until April Fools' Day?
today = date.today()
aprilFoolsDay = date(today.year, 4, 1)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if aprilFoolsDay < today:
    print(
        "April fools' day already went by, {} day(s) ago"
        .format((today - aprilFoolsDay).days)
    )
    aprilFoolsDay = aprilFoolsDay.replace(year=today.year + 1)

# TODO: Now calculate the amount of time until April Fool's Day
time_to_afd = aprilFoolsDay - today
print("It is {} days until next april fools' day".format(time_to_afd.days))
