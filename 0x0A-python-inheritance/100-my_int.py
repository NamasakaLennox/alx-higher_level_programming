#!/usr/bin/python3
"""
module containing a class that inverts '==' and '!='
"""


class MyInt(int):
    """
    A class containing methods that invert equal to and not equal to operators
    """
    def __eq__(self, other):
        """
        equal to magic method - inverts to not equal to
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        not equal to magic method - inverts to equal to
        """
        return int.__eq__(self, other)
