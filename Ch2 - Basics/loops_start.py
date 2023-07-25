def main():
    x = 0

    # TODO: define a while loop
    while (x < 5):
        print(x)
        x += 1

    # TODO: define a for loop
    for x in range(5, 10):
        print(x)

    # TODO: use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # TODO: use the break and continue statements
    for x in range(5, 10):
        if x == 7:
            break
        print(x)

    for x in range(5, 10):
        if x == 7:
            continue
        print(x)

    # TODO: using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        print(i, day)


if __name__ == "__main__":
    main()
