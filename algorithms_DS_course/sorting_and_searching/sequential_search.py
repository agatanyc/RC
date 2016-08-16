"""Implement sequential seaarch. The list is sorted."""

def sequential_search(n, xs):
    pos = 0      # starting position
    found = False
    stop = False

    while pos < len(xs) and not found and not stop:
        if xs[pos] == n:
            found = True
        else:
            if xs[pos] > n:
                stop = True
            else:
                pos += 1
    return found

if __name__ == '__main__':

    assert sequential_search(3, [3, 4, 6])
    assert  not sequential_search(5, [3, 4, 6])



