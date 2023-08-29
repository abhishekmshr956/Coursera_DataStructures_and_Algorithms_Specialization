import random
import numpy as np

def LinearSearch(A, low, high, key):
    for i in range(low, high):
        if A[i] == key:
            return i
    return "Not_Found"

m = np.random.randint(0, 100000000)
A = np.random.randint(0, m, 200000000)
# print(A)
k = np.random.randint(0, m)
print(k)
print(LinearSearch(A, 0, len(A) - 1, k))