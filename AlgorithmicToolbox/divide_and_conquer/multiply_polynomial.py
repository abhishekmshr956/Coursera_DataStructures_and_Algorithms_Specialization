def MulyPoly(A, B, n):
    product = [0] * (2*n - 1)
    for i in range(n):
        for j in range(n):
            product[i+j] += A[i] * B[j]
    return product

A = [3, 2, 5]
B = [5, 1, 3]
print(MulyPoly(A, B, len(A)))