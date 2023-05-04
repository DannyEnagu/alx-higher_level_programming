#!/usr/bin/python3
"""Defines ``7-model_state_fetch_all`` that print all
   City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    argv = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[0], argv[1], argv[2]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State) \
        .filter(City.state_id == State.id) \
        .order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
