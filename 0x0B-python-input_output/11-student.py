#!/usr/bin/python3
"""
A module that defines a class Student
"""


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

    def to_json(self, attrs=None):
        """
        Instance method that returns the dict properties of the object
        """
        if type(attrs) == list:  # check if it's a list
            for elem in attrs:
                if type(elem) != str:  # check if elements are srings
                    return (self.__dict__)

            dictionary = {}
            for num in range(len(attrs)):  # iterate through the list
                for item in self.__dict__:
                    if attrs[num] == item:
                        dictionary[item] = (self.__dict__[item])  # add item
            return (dictionary)

        return (self.__dict__)

    def reload_from_json(self, json):
        """
        replaces all attributes of a Student instance
        """
        for item in json:
            self.__dict__[item] = json[item]
