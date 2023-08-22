import numpy as np

def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for i in range(n):
        for j in range(i+1, n):
            p = numbers[i] * numbers[j]
            # if p > max_product:
            #     max_product = p
            max_product = max(max_product, p)

    return max_product

def max_pairwise_product(numbers):
    m1 = max(numbers)
    numbers.remove(m1)
    m2 = max(numbers)
    return m1 * m2

def stress_test(N, M):
    while True:
        n = np.random.randint(2, N)
        A = np.random.randint(0, M, n).tolist()
        print(A)
        result1 = max_pairwise_product_naive(A)
        result2 = max_pairwise_product(A)
        if result1 == result2:
            print("OK")
        else:
            print(f"Wrong answer: {result1}, {result2}")
            return

if __name__ == '__main__':
    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    N, M = list(map(int, input().split()))
    stress_test(N, M)
    # print(max_pairwise_product(input_numbers))