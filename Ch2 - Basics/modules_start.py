# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the math module, which contains features for working with mathematics
import math

# TODO: the math module contains lots of pre-built functions
# value = int(input("Type an integer to get the square root: "))
value = int("16")
print("The square root of {} is {}".format(value, math.sqrt(value)))

# TODO: in addition to functions, some modules contain useful constants
print("Pi is {}".format(math.pi))

# TODO: try some of the math functions for yourself here:
x = -96
print("Return the absolute value of x ({}): {}".format(x, math.fabs(x)))

x = 5
print("Return n factorial as an integer ({}): {}".format(x, math.factorial(x)))

x = 5
print(
    "Return True if x is neither an infinity nor a NaN, and False otherwise ({}): {}"
    .format(x, math.isfinite(x))
)

x = math.nan
print(
    "Return True if x is neither an infinity nor a NaN, and False otherwise ({}): {}"
    .format(x, math.isfinite(x))
)

x = float('inf')
print(
    "Return True if x is neither an infinity nor a NaN, and False otherwise ({}): {}"
    .format(x, math.isfinite(x))
)

x = 5
print(
    "Return True if x is a positive or negative infinity, and False otherwise ({}): {}"
    .format(x, math.isinf(x))
)

x = math.nan
print(
    "Return True if x is a positive or negative infinity, and False otherwise ({}): {}"
    .format(x, math.isinf(x))
)

x = float('inf')
print(
    "Return True if x is a positive or negative infinity, and False otherwise ({}): {}"
    .format(x, math.isinf(x))
)
