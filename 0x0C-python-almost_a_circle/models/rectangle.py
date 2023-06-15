#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__height * self.width)

    def display(self):
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for y in range(self.__y):
                print()
            for row in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        out = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y, self.__width,
                                                      self.__height)
        return (out)

    def update(self, *args, **kwargs):
        if (args and len(args) != 0):
            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                      self.__y)
                    else:
                        self.id = arg
                elif pos == 1:
                    self.__width = arg
                elif pos == 2:
                    self.__height = arg
                elif pos == 3:
                    self.__x = arg
                elif pos == 4:
                    self.__y = arg
                pos += 1
        elif (kwargs and len(kwargs) != 0):
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.__width, self.__height,
                                          self.__x, self.__y)
                        else:
                            self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
