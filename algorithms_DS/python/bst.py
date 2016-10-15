'''Return True if tree is a bst, Flase otherwise.'''

class Node(object):
    def __init__(self, v, l= None, r=None):
        self.value = v
        self.left = l
        self.right = r

def flat_tree(node):

    left_values  = []
    right_values = []
    all_values = []
    if node.left == None and node.right == None:
        return [node.value]
    if node.left != None:
       left_values = flat_tree(node.left)
    if node.right != None:
        right_values = flat_tree(node.right)
    all_values.extend(left_values)
    all_values.append(node.value)
    all_values.extend(right_values)
    return all_values

def is_bst(n):
    return flat_tree(n) == sorted(flat_tree(n))

if __name__ == "__main__":
  n = Node(6, Node(2, Node(1), Node(16)), Node(10, Node(5), Node(12)))
  n2 = Node(6, Node(2, Node(1), Node(3)), Node(10, Node(7), Node(12)))

  assert is_bst(n) == False
  assert is_bst(n2) == True
