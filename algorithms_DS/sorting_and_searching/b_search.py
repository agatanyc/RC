def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

seq = [1, 2, 3, 4, 5, ,6 ,7 ,8 ]
t = 5

print binary_search(seq, t)