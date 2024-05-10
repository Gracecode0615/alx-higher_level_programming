#!/usr/bin/python3
"""
Prints the first state object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not state else state.id)
