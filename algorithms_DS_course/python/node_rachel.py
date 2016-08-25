class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)
    def addLeft(self, child):
        self.left = child
    def addRight(self, child):
        self.right = child
    def setValue(self, val):
        self.value = val
    def getValue(self):
        return self.value
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

def minBST(lst):
    if len(lst) == 1:
        return Node(lst[0])
    if len(lst) == 0:
        return None
    mid = len(lst)/2
    root = Node(lst[mid])
    createLeft = minBST(lst[:mid])
    createRight = minBST(lst[mid+1:])
    root.addLeft(createLeft)
    root.addRight(createRight)
    return root

def inorder(node):
    if not node.getLeft() and not node.getRight():
        return node
    if node:
        inorder(node.getLeft())
        print node
        inorder(node.getRight())

if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 6, 7]
    print minBST(lst)
