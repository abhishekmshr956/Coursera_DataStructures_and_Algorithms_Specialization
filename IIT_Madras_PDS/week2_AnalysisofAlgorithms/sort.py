# O(n^2)
def SelectionSort(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        min_ix = i
        for j in range(i+1, n):
            if l[j] < l[min_ix]:
                min_ix = j
        (l[i], l[min_ix]) = (l[min_ix], l[i])
    return l

# O(n^2)
def InsertionSort(L):
    n = len(L)
    if n < 1:
        return L

    for i in range(n):
        j = i
        while(j>0 and L[j] < L[j-1]):
            (L[j], L[j-1]) = (L[j-1], L[j])
            j = j-1
    return L

def Insert(L, v):
    n = len(L)
    if n == 0:
        return [v]
    if v >= L[-1]:
        return L+[v]
    else:
        return Insert(L[:-1], v)+L[-1:]
    
def ISort(L):
    n = len(L)
    if n < 1:
        return L
    L = Insert(ISort(L[:-1]), L[-1])
    return L


## Merge sort
# O(n logn)
def merge(A, B):
    m, n = len(A), len(B)
    C, i, j, k = [], 0, 0, 0
    while k < m+n:
        if i == m:
            C.extend(B[j:])
            k = k + n-j
        elif j == n:
            C.extend(A[i:])
            k = k + m-i
        elif A[i] < B[j]:
            C.append(A[i])
            i, k = i+1, k+1
        else:
            C.append(B[j])
            j, k = j+1, k+1
    return C


def mergesort(A):
    n = len(A)

    if n <= 1:
        return A
    
    L = mergesort(A[:n//2])
    R = mergesort(A[n//2:])
    
    B = merge(L, R)

    return B

# Quick sort
# average run time of O(nlog n)
def quicksort(L, l, r): # Sort L[l:r]
    if r - l <= 1:
        return L
    pivot, lower, upper = L[l], l+1, l+1
    for i in range(l+1, r):
        if L[i] > pivot:
            upper += 1
        else:
            L[i], L[lower] = L[lower], L[i]
            lower, upper = lower+1, upper+1
    L[l], L[lower-1] = L[lower-1], L[l]
    lower = lower - 1
    quicksort(L, l, lower)
    quicksort(L, lower+1, upper)
    return L