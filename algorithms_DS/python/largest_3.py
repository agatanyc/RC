"""you have L, a list of numbers as input, you should process the first
M numbers in the list and return the a list with the N biggest numbers 
from the processed part of the list.

For example:
L = [3, 12, 45, 22, 19, 3, 34, 6, 9, 66]
M = 7
N = 3
R = [45, 34, 22]

The code should process the first 7 numbers ([3, 12, 45, 22, 19, 3, 34])
and return R, a list of the 3 biggest numbers,
ordered from biggest to smallest"""


def find_largest(L, M, N):
    index = M + 1
    lst = L[:index]
    lst_2 = sorted(lst, reverse=True)
    return lst_2[:N]

if __name__ == '__main__':
    L = [3, 12, 45, 22, 19, 3, 34, 6, 9, 66]
    M = 7
    N = 3
    find_largest(L, M, N)
    
    assert find_largest(L, M, N) == [45, 34, 22]

