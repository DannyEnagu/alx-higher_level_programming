#!/usr/bin/python3
"""Defines ``9-student`` module that contains
    a  Student class.
"""


class Student:
    """Defines a new class `` Student``"""
    def __init__(self, first_name, last_name, age):
        """Student Instance Constructor
           Args:
            first_name: student first name argument
            last_name: student last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary
           representation of a Student instance
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return self.__dict__
