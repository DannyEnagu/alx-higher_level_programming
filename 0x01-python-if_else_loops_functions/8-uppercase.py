#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if (ord(c)) >= (ord('a')) and (ord(c)) <= (ord('z')):
            cap = (ord(c)) - 32
            print("{}".format(chr(cap)), end="")
        else:
            print("{}".format(c), end="")

    print()
