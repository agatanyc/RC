xs = [1, 2, 3]

def f(x):
    return x * x

map(f, xs)

def f_2(a, b):
    if a > b:
        return a
    else:
        return b

reduce(f_2, xs)

    
if __name__ == '__main__':
    xs = [1, 2, 3]

    assert map(f, xs) == [1, 4, 9]
    assert reduce(f_2, xs) == 3
