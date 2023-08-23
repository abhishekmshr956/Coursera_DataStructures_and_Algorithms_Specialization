
def fibonacci(n):
    """ return nth fibonacci number"""
    if n <= 1:
        return n
    
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f
    return f[-1]

def fibonacci_naive(n):
    if n<=1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
    
def fibonacci_lastdigit(n):
    """ return last digit of the nth fibonacci number"""
    if n <= 1:
        return n
    
    f = [1, 1]
    for i in range(2, n):
        f.append((f[i-1] + f[i-2]) % 10)
    return f[-1]

# def fibonacci_mod(n, m):
#     """ return fibonacci of the nth number mod m"""
#     if n <= 1:
#         return n
    
#     previous = 0
#     current = 1
    
#     for _ in range(n-1):
#         previous, current = current, (previous + current) % m
    
#     # f = [1, 1]
#     # for i in range(2, n):
#     #     f.append((f[i-1] + f[i-2]) % m)
#     return current

if __name__ == '__main__':
    input_n = int(input())
    # input_n, input_m = map(int, input().split())
    # f = fibonacci(input_n)
    # print(f)
    # x = [a % input_m for a in f]
    # print(x)
    # print(fibonacci_mod(input_n, input_m))
    # import time
    # tic = time.perf_counter()
    print(fibonacci(input_n))
    # print(fibonacci_lastdigit(input_n))
    # print(fibonacci_naive(input_n))
    # toc = time.perf_counter()
    # print(toc-tic)