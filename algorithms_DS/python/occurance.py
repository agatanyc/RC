"""Given a sorted list find out how many times given integer occurs
   in that list."""

def occurs(xs, n):
    mid = len(xs) // 2
    count = 0
    if n < xs[mid]:
        for x in xs[: mid][::-1]:
            if x == n:
                count += 1
            else:
                break
    elif n > xs[mid]:
        for x in xs[mid + 1:]:
            if x < n:
                continue
            elif x == n:
                count += 1
            else:
                break
    if n == xs[mid]:
        count = 1
        count_right = 0
        for x in xs[mid + 1:]:
            if x == n:
                count_right += 1
            else:
                break
        for x in xs[:mid][::-1]:
            count_left = count_right
            if x == n :
                count_left += 1
            else:
                break
        count += (count_left + count_right)
    return count

assert occurs([1, 2, 3, 3, 3, 5, 6], 3) == 3
assert occurs([1, 2, 3, 3, 3, 5, 5, 6], 5) == 2
assert occurs([1, 2, 3, 3, 3, 5, 5, 6], 6) == 1
