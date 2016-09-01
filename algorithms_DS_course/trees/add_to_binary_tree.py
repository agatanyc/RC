"""Add a `Node` to binary tree."""

from min_hight_search import Node
from balanced_tree import maxDepth

def add_node(tree, node):
    # if the tree is just root add `node` to the left
    if not tree.left and not tree.right:
        tree.left = node
    # cases when the root has one child
    elif not tree.left:
        tree.left = node
    elif not tree.right:
        tree.right = node
    # case when the root has left and right child
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
    assert tree.left.value == 2
    print '_______________'
    five = Node(5)
    add_node(tree, five)
    print tree.right.value
    assert tree.right.value == 5
    print '_______________'
    eight = Node(8)
    add_node(tree, eight)
    print tree.left.left.value
    assert tree.left.left.value == 8
    print '_______________'
    one = Node(1)
    add_node(tree, one)
    print tree.right.left.value
    assert tree.right.left.value == 1




