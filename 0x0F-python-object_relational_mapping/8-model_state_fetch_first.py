#!/usr/bin/python3
"""lists first object from the database hbtn_0e_6_usa"""
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
    query = session.query(State).order_by(State.id)
    instance = query.first()
    if instance:
        print(instance.id, instance.name, sep=": ")
    else:
        print(Nothing)
