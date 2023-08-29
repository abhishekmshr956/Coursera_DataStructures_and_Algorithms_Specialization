def binary_search_recur(A, low, high, key):
    if high < low:
        return low - 1
    mid = int(low + (high - low) / 2)
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search_recur(A, low, mid-1, key)
    elif key > A[mid]:
        return binary_search_recur(A, mid + 1, high, key)
    
def binary_search_iter(A, low, high, key):
    while low <= high:
        mid = int(low + (high - low) / 2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1
    return low - 1
    

A = [7, 9, 11, 12, 15, 22]
k = int(input())
print(binary_search_recur(A, 0, len(A) - 1, k))
print(binary_search_iter(A, 0, len(A) - 1, k))