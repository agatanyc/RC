# remove node at given index from linked list

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# ll = (head, head.next)
head = Node(3)
head.next =  Node(2, Node(3, Node(6, Node(7, Node(9)))))

def delete_node(ll, index):
    if index == 0:
        return ll.next
    if ll is None:
        return None
    else:
        head = Node(ll.value)
        # recursion
        tail = delete_node(ll.next, index-1)
        head.next = tail
        return head


