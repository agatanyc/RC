from __future__ import division

def tip(n, xs):
    r = 0
    length = len(xs)
    for x in xs:
        x /= 100
        print x
        r += x
    avarage = r / length
    tip = n * avarage
    return tip

if __name__ == '__main__':
    n = 100
    xs = [10, 15, 10, 10, 25]
    print tip(n, xs)

