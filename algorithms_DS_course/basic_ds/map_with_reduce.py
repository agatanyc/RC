"""'Implementation of `map` function with `reduce`."""

def my_map(f, xs):
    ys = []
    for x in xs:
        ys.append(f(x))
    return ys


def map_with_reduce(f, xs):
    # `a` is an acumulator that initially is an empty list
    def helper(a, y):
        a.append(f(y))
        return a
    return reduce(helper, xs, [])

if __name__ == '__main__':
    def f(a):
        return a * a

    xs = [1, 2, 3]

    assert my_map(f, xs) == [1, 4, 9]
    assert map_with_reduce(f, xs) == [1, 4, 9]
