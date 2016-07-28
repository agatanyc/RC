"""Implement a queue with 2 stacks. Your queue should have an enqueue 
    and a dequeue function and it should be "first in first out" (FIFO)."""

class Stack():
    def __init__(self):
        self.items = []

    def add(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def pick(self):
        return self.items[-1]

class Queue():
    def __init__(self):
        self.items = Stack()
        self.temp = Stack()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        if self.temp.is_empty():
            for i in range(self.items.size()):
                self.temp.add(self.items.pop())
            return self.temp.pop()
        else:
            return self.temp.pop()

if __name__ == '__main__':

    s = Stack()
    s.add(5)
    s.add(6)
    s.pop()
    assert s.pick() == 5
    assert  not s.is_empty()
    assert s.size() == 1

    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print q.dequeue()
    q.enqueue(6)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
