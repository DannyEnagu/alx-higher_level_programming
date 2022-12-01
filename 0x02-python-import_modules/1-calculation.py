#!/usr/bin/python3

# execute code only when run directly and not when exported
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # create and assign value to variables
    a = 10
    b = 5

    # Print outputs
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
