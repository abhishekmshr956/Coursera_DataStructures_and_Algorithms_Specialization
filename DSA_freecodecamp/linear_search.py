def linear_search(A, target):
    """
    Returns the index position of the target if found, else returns None
    """
    n = len(A)
    for i in range(n):
        if A[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)