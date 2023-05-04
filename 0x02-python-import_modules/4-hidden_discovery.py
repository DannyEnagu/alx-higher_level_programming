#!/usr/bin/python3
import hidden_4


def main():
    """print hidden content

       Return:
           Nothing
    """
    lis_t = dir(hidden_4)
    for i in lis_t:
        if i[0] != '_':
            print("{:s}".format(i))


if __name__ == "__main__":
    main()
