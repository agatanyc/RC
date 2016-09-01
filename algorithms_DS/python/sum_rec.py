def add(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        return xs[0] + add(xs[1:])

print add([1, 2, 3])
