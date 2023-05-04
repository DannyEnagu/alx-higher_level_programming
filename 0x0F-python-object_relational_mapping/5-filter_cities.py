#!/usr/bin/python3
"""Defines a module ``5-filter_cities`` that contains a ``main``
   function that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main(argv):
    """Lists all cities of that state, using the database
       hbtn_0e_4_usa.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[0],
                         passwd=argv[1],
                         db=argv[2], port=3306)
    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id = \
                 (SELECT id FROM states WHERE name = %s) \
                 ORDER BY id ASC;", (argv[3],))
    cities = cur.fetchall()
    for i in range(len(cities)):
        for city in cities[i]:
            print(city, end="")
        if i < len(cities) - 1:
            print(', ', end="")
    print()

    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
