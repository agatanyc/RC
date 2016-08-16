"""Given 2 sorted arrays insert Binto A with merge method."""

def sorted_merge(A, B):
    leni_B = len(B)
    i = 0
    j = 0
    while j < leni_B:
        if A[i] >= B[j]:
            A.insert(i, B[j])
            j += 1
        i += 1
    return A

if __name__ == '__main__':
    A = [1, 4, 6, 8, 9]
    B = [2, 3, 7]
    print sorted_merge(A, B)
