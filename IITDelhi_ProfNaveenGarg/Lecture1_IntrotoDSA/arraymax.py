def arrayMax(A):
    """ find the maximum element in the given array
    Takes O(n) time
    """
    currentMax = A[0]
    for i in range(1, len(A)):
        if currentMax < A[i]: currentMax = A[i]
    return currentMax

if __name__ == '__main__':
    A = [7, 5, 9, 2, -1, 3, 9]
    print(arrayMax(A))