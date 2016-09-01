"""The Deque Abstract Data Type:
    """

class Deque(object):

    def __init__(self):
        """Creates a new deque that is empty.
        It needs no parameters and returns an empty deque."""
        self.items = []

    def __str__(self):
        r = []
        for x in self.items:
            r.append(str(x))
        s = ", ".join(r)
        return "[" + s + "]"

    def __str__(self):
        r = ", ".join([str(x) for x in self.items])
        return "[" + r + "]"

    def add_rear(self, x):
        return self.items.insert(0, x)

    def add_front(self, x):
        return self.items.append(x)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d = Deque()

    d.add_rear(4)
    d.add_rear(4)
    print d.__str__()
