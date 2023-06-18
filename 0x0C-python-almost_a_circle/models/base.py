#!/usr/bin/python3
"""
A module containing the base of all other classes
Manages the id attribute for other classes to avoid duplication
"""


import json
import csv
import turtle


class Base:
    """
    A class that manages the id attribute and other common dependencies for
    all other classes
    Args:
        id: the id of the object to be created
    Attributes:
        __nb_objects (int): used to set the id if id is not provided
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class id attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into json format
        Args:
            list_dictionaries (list): the list of dictionaries to be converted
        Return:
            returns the converted json string
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a converted json string into a file
        Args:
            list_objs (list): the list of objects to be saved in the file as
                              json string
        """

        filename = "{}.json".format(cls.__name__)
        if list_objs:
            dictionary = list(obj.to_dictionary() for obj in list_objs)
        else:
            dictionary = list_objs
        with open(filename, "w", encoding="utf-8") as file_open:
            file_open.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a json string into a python list of dictionary
        Args:
            json_string (str): the json string to be converted
        Return:
            returns the converted list from json
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance of a class
        Args:
            dictionary: a key value object used to create an instance
                        of a class
        Return:
            returns the created instance
        """

        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        reads a json string of instances, creates them and returns the
        instances
        Return:
            returns the list of created instances from a file
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as open_file:
                dictionary = cls.from_json_string(open_file.read())
                return list(cls.create(**item) for item in dictionary)
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves the content to a file in csv format
        Args:
            list_objs: list of objects to be added to the file in csv format
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", encoding="utf-8", newline="") as file_open:
            if list_objs is None or len(list_objs) == 0:
                file_open.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(file_open, fieldnames=fieldnames)
                for items in list_objs:
                    writer.writerow(items.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        reads data from the csv file
        Creates class objects from the file
        Return:
            returns the created objects
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8", newline="") as file_open:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dictionaries = csv.DictReader(file_open, fieldnames=fieldnames)
                dictionaries = list(dict([key, int(value)] for key, value in
                                         dicts.items()) for dicts in
                                    dictionaries)
                return list(cls.create(**dicts) for dicts in dictionaries)

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """
        draws a Rectangle or Square using the Turtle module
        Args:
            list_rectangles: a list of rectangles to draw
            list_squares: a list of squares to draw
        """
        draw = turtle.Turtle()
        draw.screen.bgcolor("#50E3E6")
        draw.pensize(4)
        draw.shape("turtle")

        # draw the rectangle
        draw.color("#E55451")
        for item in list_rectangles:
            draw.showturtle()
            draw.up()
            draw.goto(item.x, item.y)
            draw.down()
            for i in range(2):
                draw.forward(item.width)
                draw.left(90)
                draw.forward(item.height)
                draw.left(90)
            draw.hideturtle()

        # draw square
        draw.color("#666362")
        for item in list_squares:
            draw.showturtle()
            draw.up()
            draw.goto(item.x, item.y)
            draw.down()
            for i in range(2):
                draw.forward(item.width)
                draw.left(90)
                draw.forward(item.height)
                draw.left(90)
            draw.hideturtle()

            turtle.exitonclick()
