#!/usr/bin/python3
"""a script that prints state object from the database that is passed
 as argument"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    name_passed = sys.argv[4]

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()

    result = session.query(State).filter(State.name == name_passed).first()

    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()
