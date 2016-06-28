from queue import Queue

def hot(names, n):
    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(n):
            q.enqueue(q.dequeue())

        q.dequeue()
        print q.items
    return q.dequeue()

names = ['a', 'b', 'c', 'd', 'e']
n = 19

print hot(names, n)

