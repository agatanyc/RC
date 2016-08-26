"""Check if binary tree is balanced. The height of sub trees can not differ
by more then 1"""

from min_hight_search import Node

# recursively

def maxDepth(node):
    if node:
        if node.getRight() == None and node.getLeft() == None:
            node.depth = 0
            return node.depth
        else:
            node.depth = 1 + max(maxDepth(node.getLeft()), maxDepth(node.getRight()))
            return node.depth

def isBalanced(node):
    if node.getRight() == None and node.getLeft() == None:
        return True
    elif node.getRight() == None:
        return node.getLeft().getDepth() == 0
    elif node.getLeft() == None:
        return node.getRight().getDepth() == 0
    else:
        return isBalanced(node.getLeft()) and isBalanced(node.getRight()) and \
            abs(node.getRight().getDepth() - node.getLeft().getDepth()) <= 1

if __name__ == '__main__':

    two = Node(2)
    three = Node(3)
    four = Node(4)

    two.addLeft(three)

    two.addRight(four)
    maxDepth(two)
    print 'Max Depth of two: ', maxDepth(two)
    print two.depth
    print three.depth
    print four.depth
    print 'is balanced of two: ', isBalanced(two)

#___________________________

    ten = Node(10)
    five = Node(5)
    twenty = Node(20)
    seven = Node(7)
    three = Node(3)
    nine = Node(9)
    eighteen = Node(18)

    ten.addLeft(five)
    ten.addRight(twenty)
    twenty.addLeft(three)
    twenty.addRight(seven)
    three.addLeft(nine)
    three.addRight(eighteen)

    maxDepth(ten)

    print 'is balanced of ten: ', isBalanced(ten)


