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

def max_pairwise_product_1(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(1, n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i
    return numbers[index1] * numbers[index2]


def stress_test(N, M):
    np.random.seed(42)
    while True:
        n = np.random.randint(2, N)
        A = np.random.randint(0, M, n).tolist()
        # print(A)
        result1 = max_pairwise_product_naive(A)
        # result2 = max_pairwise_product(A)
        result2 = max_pairwise_product_1(A)
        if result1 == result2:
            print("OK")
        else:
            print(f"Wrong answer: {result1}, {result2}")
            return

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
    # N, M = list(map(int, input().split()))
    # stress_test(N, M)

    # a = [7, 4, 5, 7]
    # print(max_pairwise_product_1(a))