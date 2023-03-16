#!/usr/bin/python3
"""Defines a module ``my_safe_filter_states`` that contains a ``main``
   function that displays all values in the states table where name
   the last Command Line Arguments and safe from MySQL injections.
"""
import MySQLdb
import sys


def main(argv):
    """A script that lists all states names where name matches the last
    command line argument passed.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[0],
                         passwd=argv[1],
                         db=argv[2], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (argv[3],))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
