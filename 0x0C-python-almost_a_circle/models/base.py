#!/usr/bin/python3
"""
This is the base of all other classes
"""


class Base:
    """
    manages the id attribute for all other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes the id property to a given value or generated value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
