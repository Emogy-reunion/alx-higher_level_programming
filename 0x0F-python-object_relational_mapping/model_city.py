#!/usr/bin/python3
"""definition of a City class"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Maps table to the database"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
