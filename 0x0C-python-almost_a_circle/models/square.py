#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)


    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def __str__(self):
        out = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
        return (out)

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif pos == 1:
                    self.size = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
