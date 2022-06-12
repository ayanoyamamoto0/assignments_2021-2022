# Import Node class from node.py
from node import Node


# Class to represent the singly linked list in the program
class SLL:

    # Constructor to set the head (pointer to first node) to None, and size (number of nodes in the structure) to 0
    def __init__(self):
        self.head = None
        self.size = 0

    # Method to return the node in a given position in the list
    def get_node(self, pos):
        counter = 1
        tmp_node = None

        while counter <= pos:
            if counter == 1:
                tmp_node = self.head
            else:
                tmp_node = tmp_node.get_next()
            counter += 1
        return tmp_node

    # Method to add an object to the list
    def add(self, obj_data):
        if self.head is None:
            self.head = Node(obj_data, None)
        else:
            tail = self.get_node(self.size)
            new_node = Node(obj_data, None)
            tail.set_next(new_node)
        self.size += 1

    # Method to remove an object from the list
    def remove(self, pos):
        if pos == 1:
            tmp_node = self.get_node(1)
            self.head = tmp_node.get_next()
        elif pos == self.size and self.size > 1:
            tmp_node = self.get_node(pos - 1)
            tmp_node.set_next(None)
        else:
            current: Node = self.get_node(pos)
            previous: Node = self.get_node(pos - 1)
            previous.set_next(current.get_next())
        self.size -= 1

    # Method to return the size of the list
    def list_size(self):
        return self.size
