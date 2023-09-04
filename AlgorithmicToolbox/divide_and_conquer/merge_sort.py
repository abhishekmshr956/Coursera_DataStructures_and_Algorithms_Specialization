def Merge(B, C):
    D = []
    while B != [] and C != []:
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B.remove(b)
        else:
            D.append(c)
            C.remove(c)
    if B != []:
        D.extend(B)
    elif C != []:
        D.extend(C)
    return D

def MergeSort(A):
    n = len(A)
    if n == 1:
        return A
    m = n // 2
    B = MergeSort(A[0:m])
    C = MergeSort(A[m:])
    A_dash = Merge(B, C)
    return A_dash

if __name__ == '__main__':
    A = [7, 2, 5, 3, 7, 13, 1, 6]
    B = [2, 3, 5, 7]
    C = [1, 6, 7, 13]
    # print(Merge(B, C))
    print(MergeSort(A))
    