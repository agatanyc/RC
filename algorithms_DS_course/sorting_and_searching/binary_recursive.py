from __future__ import division
"""Implement binary serch recursivly."""

def binary_search(n, xs):
    found = False
    if len(xs) == 0:
        found = False
    else:
        mid = len(xs) // 2
        if xs[mid] == n:
            found = True
        elif n < xs[mid]:
            found = binary_search(n, xs[:mid])
        else:
            found = binary_search(n, xs[mid + 1:])
            
    return found

if __name__ == '__main__':

    assert binary_search(5, [3, 4, 5])
    assert not binary_search(6, [3, 4, 5])

    xs = [1, 2, 3, 4, 5]
    n = 3
    print binary_search(n, xs)
