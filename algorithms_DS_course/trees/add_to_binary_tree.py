"""Add a `Node` to binary tree."""

from min_hight_search import Node
from balanced_tree import maxDepth

def add_node(tree, node):
    if not tree.left and not tree.right:
        tree.left = node
    elif not tree.left:
        tree.left = node
    elif not tree.right:
        tree.right = node
    else:
        if maxDepth(tree.left) > maxDepth(tree.right):
            add_node(tree.right, node)
        else:
            add_node(tree.left, node)

if __name__ == '__main__':
    tree = Node(6)
    print tree
    two = Node(2)

    add_node(tree, two)
    print tree.left.value
    print '_______________'
    five = Node(5)
    add_node(tree, five)
    print tree.right.value
    print '_______________'
    eight = Node(8)
    add_node(tree, eight)
    print tree.left.left.value
    print '_______________'
    one = Node(1)
    add_node(tree, one)
    print tree.right.left.value




