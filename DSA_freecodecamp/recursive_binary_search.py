def recursive_binary_search(A, target):
    if len(A) == 0:
        return False
    else:
        mid = len(A) // 2

        if A[mid] == target:
            return True
        else:
            if A[mid] < target:
                return recursive_binary_search(A[mid+1:], target)
            else:
                return recursive_binary_search(A[:mid], target)
            
def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
