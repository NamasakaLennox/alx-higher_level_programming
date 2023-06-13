#!/usr/bin/python3
"""
A module that defines a class Student
"""


class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """
    A class that  defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the instance attributes
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Instance method that returns the dict properties of the object
        """
        return (class_to_json(self))
