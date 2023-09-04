def SelectionSort(A):
    n = len(A)
    for i in range(n):
        minindex = i
        for j in range (i+1, n):
            if A[j] < A[minindex]:
                minindex = j
        (A[i], A[minindex]) = (A[minindex], A[i])
    return A

if __name__ == '__main__':
    input_A = [7, 2, 5, 3, 7, 13, 1, 6] #, [9,3,3,2,6,5]
    print(SelectionSort(input_A))