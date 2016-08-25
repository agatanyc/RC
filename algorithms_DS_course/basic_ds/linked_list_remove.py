from node import Node

xs = ['a', 'b', 'c', 'd', 'e']
ys = [Node(x) for x in xs]

def create_pointer():
    if ys:
        for i in range(len(ys) - 1):
            ys[i].set_next(ys[i + 1])
        return ys[0]


if __name__ == '__main__':
    linked_list = create_pointer()
    ys[2].remove()
    node = ys[0]
    while node:
        print node.get_data()
        node = node.next
