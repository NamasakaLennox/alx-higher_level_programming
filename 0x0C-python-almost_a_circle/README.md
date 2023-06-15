# 0x0C. Python - Almost a circle

## tests/
All your files, classes and methods must be unit tested and be PEP 8 validated.

## models/base.py, models/__init__.py
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

## models/rectangle.py
Write the class Rectangle that inherits from Base:

Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

## models/square.py
Write the class Square that inherits from Rectangle:

Update the class Square by adding the public getter and setter size

Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

## models/rectangle.py
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

## models/square.py
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

## models/base.py
Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries

Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
