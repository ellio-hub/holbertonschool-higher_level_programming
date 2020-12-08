#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if (number < 0):
    x = (number * -1) % 10
if (x == 0):
    s = ("Last digit of {} is {} and is 0")
elif (x > 5):
    s = ("Last digit of {} is {} and is greater than 5")
else:
    s = ("Last digit of {} is {} and is less than 6 and not 0")
print (s.format(number, x))
