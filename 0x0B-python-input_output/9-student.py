#!/usr/bin/python3
"""
defines a class Student
"""


class Student:
    """class representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student properties"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
