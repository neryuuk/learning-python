# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10 / 0

# TODO: Exceptions provide a way of catching errors and then handling them in
# a separate section of the code to group them together
try:
    x = 10 / 0
except:
    print("Well, that didn't work!")

# TODO: You can also catch specific exceptions
try:
    x = "10" / 0
except ZeroDivisionError:
    print("Can't divide by zero now, can we?")
except TypeError:
    print("Well, that didn't work!")

try:
    answer = input("What should I divide 10 by? ")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError:
    print("Can't divide by zero now, can we?")
except ValueError as error:
    print("Well, '{}' isn't a number now, is it?".format(answer))
    print(error)
finally:
    print("This always runs")
