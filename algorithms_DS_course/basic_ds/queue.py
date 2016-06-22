"""Implement a `Queue` data structure."""

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__name__':
    q = Queue()
    q. enqueue('a')
    q. enqueue('b')
    q. enqueue('c')
    q.dequeue()

    print q.size()
    assert q.size() == 2

