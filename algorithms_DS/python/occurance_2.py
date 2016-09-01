"""Given a sorted list find out how many times given integer occurs
   in that list."""

def occurs(xs, n):
    mid = len(xs) // 2     # the middle point of the arrey
    count = 0
    if n < mid:
        for x in xs[:mid]:
            if n == x:
                count += 1
        return count

xs = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
n = 2
print occurs(xs, n)
