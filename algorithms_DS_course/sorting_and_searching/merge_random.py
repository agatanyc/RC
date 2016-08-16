from __future__ import division
from random import randint

"""Generate a random list of integers. Show how this list is sorted by the
   merge sort."""

# list to be sorted
xs = [randint(0, 30) for x in range(10)]

def merge_list(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        # divide the given list in half recursively
        mid = len(xs) // 2
        left_half = xs[:mid]
        right_half = xs[mid:]
        print "before"
        print right_half, left_half

        merge_list(left_half)
        merge_list(right_half)

        i = 0  # left half
        j = 0  # right half
        k = 0  # merged list
        print "after"
        print right_half, left_half

        # Now operate on two sorted lists

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                xs[k] = left_half[i]
                i += 1
                k += 1
            else:
                xs[k] = right_half[j]
                j += 1
                k += 1

        while i < len(left_half):
            xs[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            xs[k] = right_half[j]
            j += 1
            k += 1
    return xs





if __name__ == '__main__':
    print merge_list(xs)
