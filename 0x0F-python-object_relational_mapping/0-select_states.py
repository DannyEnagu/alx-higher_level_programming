#!/usr/bin/python3
"""Defines a module ``select_state`` that contains a ``main``
   function that lists all states from a database passed as
   Command Line Arguments.
"""
import MySQLdb
import sys


def main(argv):
    """A script that lists all states from the database
       hbtn_0e_0_usa:
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[0],
                         passwd=argv[1],
                         db=argv[2], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main(sys.argv[1:])
