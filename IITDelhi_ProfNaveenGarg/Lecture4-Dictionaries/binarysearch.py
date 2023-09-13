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

import numpy as np
if __name__ == '__main__':
    # np.random.seed(42)
    A = np.sort(np.random.randint(-10, 10, 10)).tolist()
    print(A)
    target = np.random.randint(-10, 10)
    print(target)
    print(binary_search(A, target))