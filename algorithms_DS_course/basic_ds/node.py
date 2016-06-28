"""Implementation of `Node` class."""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
