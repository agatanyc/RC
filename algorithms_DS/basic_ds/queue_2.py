"""Implement the Queue ADT, using a list such that the rear of the queue is at
the end of the list"""

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(-1, item)

    def dequeue(self):
        self.items.remove(self.items[0])

    def size(self):
        return len(self.items)
