def binary_search(A, target):
    """ returns the index of the target. if target not found, then returns the index where it should be placed"""
    n = len(A)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
    return low 

def linear_search(A, target):
    n = len(A)
    for i in range(n):
        if target == A[i]:
            return i
    return "Not found"

import numpy as np
if __name__ == '__main__':
    # np.random.seed(42)
    # A = np.sort(np.random.randint(-10, 10, 10)).tolist()
    B = np.random.randint(-10, 10, 10).tolist()
    print(B)
    target = np.random.randint(-10, 10)
    print(target)
    print(linear_search(B, target))