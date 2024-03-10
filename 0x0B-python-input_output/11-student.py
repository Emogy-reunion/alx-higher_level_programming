#!/usr/bin/python3
"""
contains the class Student
"""


class Student:
    """template of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """this replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
