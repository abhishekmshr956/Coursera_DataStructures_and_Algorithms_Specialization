import numpy as np

def gcd_naive(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd(a, b):
    a, b = min(a,b), max(a,b)
    if b % a == 0:
        return a
    else:
        return gcd(a, b % a)
    
def stress_test(N, M):
    while True:
        p, q = np.random.randint(1, M, N)
        result1 = gcd_naive(p, q)
        result2 = gcd(p, q)
        if result1 == result2:
            print("Ok")
        else:
            print(f"Wrong answer: gcd for {p, q}: naive: {result1}, fast: {result2}")
            return


def custom_test(f):
    test_cases = [(128, 96), (22, 26), (360, 210), (108, 144), (2, 24), (1,5), (6,14)]
    test_results = [32, 2, 30, 36, 2, 1, 2]
    for i in range(len(test_cases)):
        p, q = test_cases[i]
        result = f(p, q)
        if result == test_results[i]:
            print(f"OK: gcd of {test_cases[i]} = {result}")
        else:
            print(f"Wrong answer: gcd of {test_cases[i]} is {test_results[i]} but the function returned {result}")

if __name__ == '__main__':
    # a, b = map(int, input().split())
    # print(gcd_naive(a, b))
    # custom_test(gcd)
    stress_test(2, 100000)