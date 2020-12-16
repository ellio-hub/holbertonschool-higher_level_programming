#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for i in range(len(names)):
        name = names[i]
        if(name[0] != '_'):
            print("{}".format(name))

if __name__ == "__main__":
    main()
