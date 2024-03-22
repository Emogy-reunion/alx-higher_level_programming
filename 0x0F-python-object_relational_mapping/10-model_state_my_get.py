#!/usr/bin/python3
"""prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == "__main__":
    """maps class"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == (sys.argv[4],))
    instance = query.one()
    if instance is None:
        print("Not found")
    else:
        print(instance.id)
