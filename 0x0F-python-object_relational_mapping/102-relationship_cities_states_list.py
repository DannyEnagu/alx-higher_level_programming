#!/usr/bin/python3
"""Defines ``7-model_state_fetch_all`` that list all
   State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    argv = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[0], argv[1], argv[2]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
