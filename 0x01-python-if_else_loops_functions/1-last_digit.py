#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    x = ((number * -1) % 10) * -1
else:
    x = number % 10
if (x == 0):
    s = ("and is 0")
elif (x > 5):
    s = ("and is greater than 5")
elif (x < 6 and x != 0):
    s = ("and is less than 6 and not 0")
print ("Last digit of {:d} is {:d} {}".format(number, x, s))
