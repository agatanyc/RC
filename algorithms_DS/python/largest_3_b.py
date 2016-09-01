"""you have L, a list of numbers as input, you should process the first
M numbers in the list and return the a list with the N biggest numbers 
from the processed part of the list.

The L list is generated one by one.
L = [3, 12, 45, 22, 19, 3, 34, 6, 9, 66]
M = 7
N = 3
R = [45, 34, 22]

The code should process the first 7 numbers ([3, 12, 45, 22, 19, 3, 34])
and return R, a list of the 3 biggest numbers,
ordered from biggest to smallest"""

def find_largest_3(L, M, N):
    r = [0, 0, 0]
    i = 0
    while i < 7:
        n = L[i]
        m = min(r)
        if n > m:
            r.remove(m)
            r.append(n)
        i += 1
    return sorted(r, reverse=True)

if __name__ == '__main__':
    L = [3, 12, 45, 22, 19, 3, 34, 6, 9, 66]
    M = 7
    N = 3
    print find_largest_3(L, M, N)
    
    assert find_largest_3(L, M, N) == [45, 34, 22]
