"""Implementation of an `OrderedList` class."""
from unordered_list import UnorderedList
from node import Node


class OrderedList(object):
    def __init__(self):
        self.head = None

    def is_empty():
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:   #empty list
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(item)
  
