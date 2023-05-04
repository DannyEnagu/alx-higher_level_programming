#!/usr/bin/python3
from sys import argv


def main():
    """program that prints the number of and the
        list of its arguments

        Returns:
            Nothing
    """
    if len(argv) == 1:
        print("{:d} {:s}.".format(0, "arguments"))
    elif len(argv) == 2:
        print("{:d} {:s}:".format(1, "argument"))
    else:
        print("{:d} {:s}:".format((len(argv) - 1), "arguments"))

    if len(argv) > 1:
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    main()
