#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for c in str:
        if (ord(c)) >= (ord('a')) and (ord(c)) <= (ord('z')):
            cap = (ord(c)) - 32
            new_str += chr(cap)
        else:
            new_str += c
    print("{:s}".format(new_str))
