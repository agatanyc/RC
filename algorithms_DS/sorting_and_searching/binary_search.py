from __future__ import division
"""Implement binary search."""

def binary_search(n, xs):

    found = False
    first = 0
    last = len(xs) - 1

    while first <= last and not found:
        mid = (first + last) // 2

        if  xs[mid] == n:
            found = True
        else:
            if n < xs[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

if __name__ == '__main__':

    assert binary_search(3, [3, 4, 5])
    assert not binary_search(9, [3, 4, 5])

