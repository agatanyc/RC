# -*- coding: utf-8 -*-
"""10/1 — Intersperse
Write a function that takes a list of lists and intersperses their elements, e.g.
intersperse([[1,2,3], [4,5,6], [7,8,9]]) => [1,4,7,2,5,8,3,6,9]"""

def unfold(xs):
    r = []
    for x in xs:   # sublist
        for n in x: # elements of a sublist 
            r.append(n)
    return r

def intersperse(xs):
    r = []
    for i in range(len(xs[0])):
        for x in xs:
            r.append(x[i])
    return r

# modify problem to allow the sublist be different length
def intersperse_2(ys):
    r = []
    range_length = len(max(ys, key=len))
    for i in range(range_length):
        for y in ys:
            if i < len(y):
                r.append(y[i])
    return r

if __name__ == '__main__':

    xs = [[1,2,3], [4,5,6], [7,8,9]]
    assert unfold(xs) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert intersperse(xs) ==[1, 4, 7, 2, 5, 8, 3, 6, 9]

    ys = [[1,2,3,7], [4,6], [7,8,9]]
    intersperse_2(ys)
    assert intersperse_2(ys) ==[1, 4, 7, 2, 6, 8, 3, 9, 7]


