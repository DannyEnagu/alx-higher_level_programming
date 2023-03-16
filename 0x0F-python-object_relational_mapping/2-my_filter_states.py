#!/usr/bin/python3
"""Defines a module ``filter_states`` that contains a ``main``
   function that displays all values in the in state table that
   matches the last Command Line Arguments.
"""
import MySQLdb
import sys


def main(argv):
    """A script that displays all values thet matches the last
    command line argument passed.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[0],
                         passwd=argv[1],
                         db=argv[2], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY \
                 id ASC", (argv[3],))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
