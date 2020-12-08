#!/usr/bin/python3
for i in range(99):
    if (i < 10):
        j = 0
    else:
        j = ''
    print("{}{}, ".format(j, i), end='')
print("{}".format(i + 1))
