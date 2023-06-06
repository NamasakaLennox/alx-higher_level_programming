#!/usr/bin/python3
"""
A module containing the class Rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a Rectangle with two properties
    The properties are it's width and height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the private attributes width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        getter method for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method for the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter method for the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance method, finds the area of the Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        public instance method, finds the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        returns the rectangle printed with a '#' character
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)
        for x in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"

        return (string[:-1])

    def __repr__(self):
        """
        returns a string representation of rectangle
        can be used to create a new instance using eval()
        """
        str_tuple = (self.__width, self.__height)
        string = "Rectangle" + str(str_tuple)
        return (string)

    def __del__(self):
        """
        print message when instance is deleted
        """
        type(self).number_of_instances -= 1
        del self
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method that finds the largest of the 2 rectangles
        returns the largest of the two
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        creates an instance of the Rectangle class
        """
        new = cls(size, size)
        return new
