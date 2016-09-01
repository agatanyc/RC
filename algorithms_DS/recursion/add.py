def list_sum(xs):
    if len(xs) = 1:
        return xs[0]
    else:
        return xs[0] + list_sum(xs[1: ])

if __name__ == '__main__':

    xs == [1, 2, 4]
    print list_sum(xs)
