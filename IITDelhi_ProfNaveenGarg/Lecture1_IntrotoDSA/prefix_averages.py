"""
    comparing two algorithms with run time n^2 and n.
    input: an n-element array A of numbers
    output: an n-element array A of numbers such that A[i] is the average of elements X[0], ......, X[i]
"""

def prefixAverages1(A):
    """ O(n^2)"""
    n = len(A)
    B = [None] * n
    for i in range(n):
        a = 0
        for j in range(0, i+1):
            a = a + A[j]
        B[i] = a / (i + 1)
    return B

def prefixAverages2(A):
    """ O(n) """
    n = len(A)
    B = [None] * n
    s = 0
    for i in range(n):
        s = s + A[i]
        B[i] = s / (i+1)
    return B


if __name__ == '__main__':
    X = [4, 5, 10, 12, 8]
    print(X)
    print(prefixAverages1(X))
    print(prefixAverages2(X))
        