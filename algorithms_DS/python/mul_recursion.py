def multiplay(a, b):
    """Multiplay two elements w/o using `*`"""
    if a == 1:
        return b
    return b + multiplay(a - 1, b)
