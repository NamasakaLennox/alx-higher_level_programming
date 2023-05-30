#!/usr/bin/python3
"""
A module for a singly linked list using python classes
"""


class Node:
    """
    A class Node that is used to create a node in a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        a method that initializes the data and next node attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter method for the data attribute
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        setter method for the data attribute
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter method for the next_node attribute
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        setter method for next_node attribute
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    a class that creates a singly linked list
    """
    def __init__(self):
        """
        initializes the head attribute to None
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        method to insert items in a list in a sorted order
        """
        new = Node(value)
        temp = self.__head

        if not self.__head:  # if it's the first item in list
            self.__head = new
            new.next_node = None
        else:
            if value < self.__head.data:  # add node at the beginning of list
                new.next_node = temp
                self.__head = new
            else:  # add node anywhere else in the program
                while temp.next_node and temp.next_node.data < value:
                    temp = temp.next_node
                new.next_node = temp.next_node
                temp.next_node = new

    def __str__(self):
        """
        prints the list each item per line
        """
        string = ""
        current = self.__head

        while current:
            string += str(current.data)
            current = current.next_node
            if current:
                string += "\n"
        return (string)
