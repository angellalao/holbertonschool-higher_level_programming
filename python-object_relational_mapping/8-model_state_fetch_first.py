#!/usr/bin/python3
"""a script that prints the first state object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()

    result = session.query(State).order_by(State.id).first()

    if result:
            print(f"{result.id}: {result.name}")
    else:
        print("Nothing\n")
    session.close()
