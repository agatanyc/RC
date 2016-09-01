from __future__ import division
from random import randint

"""Generate a random list of integers. Show how this list is sorted by the
   merge sort."""

# list to be sorted
xs = [randint(0, 30) for x in range(10)]

def merge_list(xs):
    if len(xs) == 1:
        return [xs[0]]
    else:
        # divide the given list in half, recursively
        mid = len(xs) // 2
        left_half = xs[:mid]
        right_half = xs[mid:]
        print "before"
        print right_half, left_half

        sorted_left_half = merge_list(left_half)
        sorted_right_half = merge_list(right_half)

        print "after"
        print sorted_right_half, sorted_left_half

        # Now operate on two sorted lists
        sortedl = []
        while len(sorted_left_half) > 0 and len(sorted_right_half) > 0:
            if sorted_left_half[0] < sorted_right_half[0]:
                sortedl.append(sorted_left_half.pop(0))
            else:
                sortedl.append(sorted_right_half.pop(0))

        while len(sorted_left_half) > 0:
            sortedl.append(sorted_left_half.pop(0))

        while len(sorted_right_half) > 0:
            sortedl.append(sorted_right_half.pop(0))
    return sortedl


if __name__ == '__main__':
    print merge_list(xs)
