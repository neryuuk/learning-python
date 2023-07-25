from datetime import date, datetime


def main():
    # DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today is {}".format(today))

    # TODO: print out the date's individual components
    print("Date components:", today.day, today.month, today.year)

    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is {}".format(today.weekday()))
    days = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]
    print("Which is a {}".format(days[today.weekday()]))

    # DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is {}".format(today))

    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("The current time is {}".format(t))


if __name__ == "__main__":
    main()
