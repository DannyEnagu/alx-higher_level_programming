#!/usr/bin/python3
"""Defines a module ``cities_by_state`` that contains a ``main``
   function that list all cities from a database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main(argv):
    """lists all cities from the database hbtn_0e_4_usalists all
       cities from the database hbtn_0e_4_usa.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[0],
                         passwd=argv[1],
                         db=argv[2], port=3306)
    cur = db.cursor()
    cur.execute("SELECT city.id, city.name, state.name FROM cities AS \
                 city INNER JOIN states AS state \
                 ON city.state_id = state.id \
                 ORDER BY city.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1:])
