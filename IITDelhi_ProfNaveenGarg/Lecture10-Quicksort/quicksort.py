def Partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[j], A[l] = A[l], A[j]
    return j

def QuickSort(A, l, r):
    if l >= r:
        return
    m = Partition(A, l, r)
    QuickSort(A, l, m-1)
    QuickSort(A, m+1, r)


import random
def RandomQuickSort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    m = Partition(A, l, r)
    QuickSort(A, l, m-1)
    QuickSort(A, m+1, r)

if __name__ == '__main__':
    A = [17, 12, 6, 19, 23, 8, 5, 10]
    QuickSort(A, 0, len(A) - 1)
    print(A)

    A = [17, 12, 6, 19, 23, 8, 5, 10]
    print(A)
    RandomQuickSort(A, 0, len(A) - 1)
    print(A)
    # print(Partition(A, 0, len(A) - 1))
    # print(A)