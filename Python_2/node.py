# Class to represent the node in the program
class Node:

    # Constructor to assign 2 values to the Node object
    # Parameters are: obj, pointer_next
    def __init__(self, obj, pointer_next):
        self.obj = obj
        self.pointer_next = pointer_next

    # Method to return the data object
    def get_data(self):
        return self.obj

    # Method to save the data object
    def set_data(self, obj):
        self.obj = obj

    # Method to get the link to the next node
    def get_next(self):
        return self.pointer_next

    # Method to set the link to the next node
    def set_next(self, node_next):
        self.pointer_next = node_next
