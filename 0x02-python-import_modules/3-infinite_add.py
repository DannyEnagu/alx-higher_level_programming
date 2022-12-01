#!/usr/bin/python3
from sys import argv


def main():
    """program that prints the result of the addition
        of all arguments
       Return:
            Nothing
    """
    total_sum = 0
    if len(argv) == 1:
        print("{:d}".format(total_sum))
    else:
        for i in range(1, len(argv)):
            total_sum += int(argv[i])
        print("{:d}".format(total_sum))


if __name__ == "__main__":
    main()
