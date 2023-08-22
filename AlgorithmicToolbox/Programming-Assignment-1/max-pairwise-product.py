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

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))