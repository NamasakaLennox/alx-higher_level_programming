#!/usr/bin/python3
"""
A module that defines a class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    A class that defines a Rectangle with it's properties
    Inherits attributes of the class 'Base'
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle with it's properties
         Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): position horizontally
            y (int): position vertically
            id: the id of the object
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        A getter method for the width attribute
        Return:
            returns the width of the object
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        A setter method for the width property
        Args:
            value: the value of the width
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        A getter method for the height property
        Return:
            returns the value of the height property of the object
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        A setter method for the height property
        Args:
            value: the value of the height attributes
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        A getter method for the x attribute
        Return:
            returns the value of x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        A setter method for the x attribute
        Args:
            value: the value of x to be set
        """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        A getter method for y property
        Return:
            returns the value of y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        A setter method for the y attribute
        Args:
            value: the value of the y attribute
        """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes the area of the object(Rectangle)
        Return:
            returns the computed area
        """
        return (self.__height * self.width)

    def display(self):
        """
        Displays the rectangle using the '#' symbol
        Prints the rectangle on the standard output
        """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for y in range(self.__y):
                print()
            for row in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        """
        Overloads __str__ and returns a formated output of the Rectangle
        Return:
            returns the formatted output
        """
        out = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y, self.__width,
                                                      self.__height)
        return (out)

    def update(self, *args, **kwargs):
        """
        Updates the values of an object given the new values to set the object
        Only sets args values if both optional arguments exist
        Args:
            args (optional): non keyworded arguments
            kwargs (optional): key worded arguments
        """
        if (args and len(args) != 0):
            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x,
                                      self.y)
                    else:
                        self.id = arg
                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1
        elif (kwargs and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height,
                                      self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Sets the values of the object into a dictionary representation
        Return:
            the dictionary containing all the attributes of the object
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
