# regular recursion

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)

# factorial tail recursive -> use of accumulator

def fac_tail_rec(n, acc=1):
    if n <= 1:
        return acc
    else:
        return fac_tail_rec(n-1, acc*n)

assert fac_tail_rec(5) == 120
