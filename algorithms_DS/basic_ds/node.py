"""Implementation on a `Node` class."""

class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def remove(self):
        next_node = self.get_next()
        data = next_node.get_data()
        self.set_data(data)
        self.set_next(next_node.get_next())

if __name__ == '__main__':
    n = Node(5)
    m = 7
    
    print n.get_data()
    print n.get_next()
    n.set_next(m)
    print n.get_next().get_data()
    print n.remove()



