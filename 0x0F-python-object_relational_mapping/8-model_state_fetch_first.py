#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Replace placeholders with actual MySQL credentials
    username, password, database_name = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}")

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to fetch the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

