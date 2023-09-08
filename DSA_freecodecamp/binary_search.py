def binary_search(A, target):
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
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)