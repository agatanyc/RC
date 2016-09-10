"""
Write a function that takes a list of numbers, and returns the longest
consecutive sublist of strictly increasing or decreasing numbers.

straight([1, 3, 3, 5, 6, 4, 2, 1, 7])
-> [6, 4, 2, 1]
([1, 3, 3, 5, 6] is not strictly increasing, because of the repeated 3s)
If there are multiple increasing/decreasing sublists of the same length,
return whichever one you like.
"""

def straight(xs):
    """Return the longest strictly increasing or decreasing sublist of xs."""
    n = len(xs)
    if n < 2:
        return xs
    r = []
    i = 0           # first index of current sublist
    while i < n - 1:
        j = i + 1
        if xs[i] == xs[j]:
            if not r:
                r = xs[i:j]
            i = j  # We're done here.  Move on to the next sublist.
        else:
            if xs[i] < xs[j]:
                while j < n and xs[j-1] < xs[j]:
                    j += 1
            else:
                while j < n and xs[j-1] > xs[j]:
                    j += 1
            # Now, j in the lowest index NOT in the sublist.
            if j - i > len(r):
                r = xs[i:j]
            i = j - 1
    return r

if __name__ == '__main__':
    assert [6, 4, 2, 1] == straight([1, 3, 3, 5, 6, 4, 2, 1, 7]
