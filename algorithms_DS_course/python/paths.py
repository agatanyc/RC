"""Find number of paths between two opposite corners of the grid."""

def paths(x, y):
    """x, y - cell coordinatesn"""
    count = 0
    if x == 0 and y == 0:
        count += 1
    if x > 0:
        count += paths(x - 1, y)
    if y > 0:
        count += paths(x, y - 1)
    return count

print paths(4, 4)
print paths(1, 1)
print paths(0, 0)
