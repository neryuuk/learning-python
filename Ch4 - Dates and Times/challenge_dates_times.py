import calendar


def main():
    while (True):
        weekday = validWeekday()
        year = validYear()
        month = validMonth()
        countOcurrences(weekday, year, month)


def validWeekday():
    while (True):
        print("Which day of the week do you want to count?")
        for i, day in enumerate(calendar.day_name):
            print("{}: {}".format(i, day))
        print("Or 'exit' to quit")
        userInput = input("? ")
        if userInput == 'exit':
            exit(0)
        try:
            weekday = int(userInput)
            if weekday < 0 or weekday > 6:
                raise ValueError()
            return weekday
        except:
            print("Invalid value for the week: {}\n".format(userInput))
            continue


def validYear():
    while (True):
        userInput = input("Enter year or 'exit' to quit: ")
        if userInput == 'exit':
            exit(0)
        try:
            year = int(userInput)
            if year < 0:
                raise ValueError()
            return year
        except:
            print("Invalid value for the year: {}\n".format(userInput))
            continue


def validMonth():
    while (True):
        userInput = input("Enter month or 'exit' to quit: ")
        if userInput == 'exit':
            exit(0)
        try:
            month = int(userInput)
            if month < 1 or month > 12:
                raise ValueError()
            return month
        except:
            print("Invalid value for the month: {}\n".format(userInput))
            continue


def countOcurrences(weekday, year, month):
    count = 0
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        count += 1 if week[weekday] else 0
    print("There are {} {}s in {} of {}".format(
        count,
        list(calendar.day_name)[weekday],
        list(calendar.month_name)[month],
        year
    ))
    print("-----------\n")


if __name__ == "__main__":
    main()
