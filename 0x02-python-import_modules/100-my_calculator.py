#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    """Basic calculator that adds, subtract,
        multiply and divide two number

       Return:
        Nothing
    """
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opt = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] not in list(opt.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, opt[argv[2]](a, b)))


if __name__ == "__main__":
    main()
