"""Implementation of an `Unordered List`.
 Unordered list is built from a collection of nodes, each linked to the next by explicit references"""

from node import Node

class UnorderedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item) # temp is a Node instance
        temp.set_next(self.head)

        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        if current:
            while current:
                previous = current
                current = current.get_next()

        previous.set_next(temp)

if __name__ == '__main__':

    un = UnorderedList()
    assert un.is_empty()
    un.append(7)
"""
    un.add(5)
    un.add(9)

    assert un.size() == 2
    assert un.search(9) 
    assert not un.search(6) 

    un.remove(9)
    assert un.size()== 1

    un.append(8)
    assert un.size() == 2
    """
