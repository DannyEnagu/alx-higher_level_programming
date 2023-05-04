#!/usr/bin/python3

# execut code only when run directly
if __name__ == "__main__":
    from add_0 import add

    # Create and assign values to parameters
    a = 1
    b = 2

    # Print ouput
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
