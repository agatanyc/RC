"""Write two Python functions to find the max number in a list.
The first function should compare each number to every other number
on the list. O(n2)O(n2). The second function should be linear O(n)O(n)."""

def compare_1(xs):
    r = 0
    for x in xs:
        xs.remove(x)
        ys = xs
        for y in ys:
            if y > x and y > r:
                r = y
    return r

def compare_2(xs):
    r = 0
    for x in xs:
        if x > r:
            r = x
    return r

xs = [1, 2, 3, 5, 8, 10, 4]
print compare_1(xs)
print compare_2(xs)
    
