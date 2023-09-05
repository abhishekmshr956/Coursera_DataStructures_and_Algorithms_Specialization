def Partition(A, l, r):
    x = A[l] # pivot
    j = l
    for i in range(l + 1, r+1):
        if A[i] <= x:
            j = j + 1
            (A[j], A[i]) = (A[i], A[j])
    (A[l], A[j]) = (A[j], A[l])
    return j

def QuickSort(A, l, r):
    if l >= r:
        return
    m = Partition(A, l, r)
    QuickSort(A, l, m - 1)
    QuickSort(A, m + 1, r)

if __name__ == '__main__':
    # A = [7, 2, 5, 3, 7, 13, 1, 6]
    A = [9,3,3,2,6,5]
    # print(Merge(B, C))
    QuickSort(A, 0, len(A) - 1)
    print(A)
