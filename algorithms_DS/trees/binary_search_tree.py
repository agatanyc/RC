"""Check if binary tree is a binary search tree."""

from min_hight_search import Node

def is_b_search(node):
    if not node.left and not node.right:
        return True
    elif not node.left:
        if node.right.value < node.value:
           return False
        else:
            return is_b_search(node.right)
    elif not node.right:
        if node.left.value > node.value:
            return False
        else:
            return is_b_search(node.left)
    else:
        if node.left.value > node.value or node.right.value < node.value:
            return False
        else:
            return is_b_search(node.left) and is_b_search(node.right)

if __name__ == '__main__':

    two = Node(2)
    two.addLeft(Node(1))
    four = Node(4)
    two.addRight(four)
    four.addLeft(Node(3))
    four.addRight(Node(5))

    print is_b_search(two)


    two = Node(2)
    two.addLeft(Node(1))
    four = Node(4)
    two.addRight(four)
    four.addLeft(Node(7))
    four.addRight(Node(5))

    print is_b_search(two)


