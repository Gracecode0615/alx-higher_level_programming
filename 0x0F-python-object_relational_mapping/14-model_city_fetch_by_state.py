#!/usr/bin/python3
"""[summary]
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # HERE: no SQL query, only objects!
    session = Session()

    for i in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(i.state.name, i.id, i.name))

    session.close()
