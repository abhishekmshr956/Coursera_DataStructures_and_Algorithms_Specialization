def gcd_naive(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def custom_test():
    test_cases = [(128, 96), (22, 26), (360, 210), (108, 144), (2, 24), (1,5), (6,14)]
    test_results = [32, 2, 30, 36, 2, 1, 2]
    for i in range(len(test_cases)):
        p, q = test_cases[i]
        result = gcd_naive(p, q)
        if result == test_results[i]:
            print(f"OK: gcd of {test_cases[i]} = {result}")
        else:
            print(f"Wrong answer: gcd of {test_cases[i]} is {test_results[i]} but the function returned {result}")

if __name__ == '__main__':
    # a, b = map(int, input().split())
    # print(gcd_naive(a, b))
    custom_test()