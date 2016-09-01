"""This module represents linked lists as chained pairs (i.e., tuples).  The
empty list is represented by None.

The first element of a list is called the 'head', and the sublist of remaining
elements is called the 'tail'.  """

def cons(x, xs=None): # Construct a linked list
    """Return a list having the specified head and tail."""
    if xs:
        assert type(xs) == tuple
    return (x, xs)

def head(xs):
    """Return the first element of list `xs`."""
    assert type(xs) == tuple
    return xs[0]

def tail(xs):
    """Return a list of all `xs` except the first."""
    assert type(xs) == tuple
    return xs[1]

# Purely functional implementation
def size(xs):
    """Return the number of elements in list `xs`."""
    if xs == None:
        return 0
    else:
        assert type(xs) == tuple
        return 1 + size(tail(xs))

# Imperative implementation
def size_loop(xs):
    """Return the number of elements in list `xs`."""
    r = 0
    while xs:
        assert type(xs) == tuple
        r += 1
        xs = tail(xs)
    return r

def is_empty(xs):
    return xs == None
