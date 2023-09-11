"""
Insertion Sort: key idea and pseudo code
Use two variables i and j
Array is sorted from A[0] to A[j-1]
Pseudo code:
for j from 1 to n-1 do
    key = A[j]
    insert A[j] into the sorted sequence A[1,j-1]
    i = j - 1
    while i > -1 and A[i] > key:
        do A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
"""

def InsertionSort(A):
    """ sorts given array using insertion sort
    Best case: array is already sorted, run time is O(n)
    Worst case: array is in descending order, run time is O(n^2)
    Average case: run time is O(n^2)
    """

    for j in range(1, len(A)):
        print(A)
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i + 1] = key
    
    return A

import numpy as np

if __name__ == '__main__':
    # np.random.seed(42)
    A = np.random.randint(-10,20, 5).tolist()
    InsertionSort(A)
    print(A)
