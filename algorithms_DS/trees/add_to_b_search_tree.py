"""Add a node to a binary search (but not balanced) tree."""

from min_hight_search import Node

def add_node(tree, node):
    if not tree.left and not tree.right:
        if tree.value > node.value:
            tree.left = node
        else:
            tree.right = node
    elif tree.left and node.value > tree.value:
        add_node(tree.right, node)
    elif tree.left and node.value < tree.value:
        add_node(tree.left, node)
    elif tree.right and node.value < tree.value:
        add_node(tree.left, node)
    elif tree.right and node.value > tree.value:
        add_node(tree.right, node)
        
if __name__ == '__main__':

    tree = Node(5)
    four = Node(4)
    six = Node(6)
    tree.addLeft(four)
    tree.addRight(six)
    seven = Node(7)

    add_node(tree, seven)
    assert tree.right.right.value == 7

    one = Node(1)
    add_node(tree, one)
    assert tree.left.left.value == 1

    three = Node(3)
    add_node(tree, three)
    assert tree.left.left.right.value == 3






