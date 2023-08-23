def fibonacci(n):
    if n<=1:
        return n
    
    previous, current = 0, 1

    for _ in range(n-1):
        previous, current = current, previous + current

    return current

def sum_of_fibonacci_last_digit_1(n):
    last_digit = (fibonacci(n+2) - 1) % 10
    return last_digit

def sum_of_fibonacci_partial_last_digit_1(m, n):
    sum_m = fibonacci(m+1) - 1
    sum_n = fibonacci(n+2) - 1
    return (sum_n - sum_m) % 10

def find_pisano_period(m):
    previous = 0
    current = 1

    period = 0

    for i in range(m*m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return period + 1
        period += 1

def huge_fibonacci(n, m):
    if n<=1:
        return n
    
    pisano_period = find_pisano_period(m)
    n %= pisano_period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current % m

def sum_of_fibonacci_last_digit(n):
    last_digit = huge_fibonacci(n+2, 10) - 1
    if last_digit == -1:
        return 9
    else:
        return last_digit
    
def sum_of_fibonacci_partial_last_digit(m, n):
    last_digit_m = sum_of_fibonacci_last_digit(m-1)
    last_digit_n = sum_of_fibonacci_last_digit(n)
    last_digit = last_digit_n - last_digit_m
    if last_digit < 0:
        last_digit += 10
    return last_digit

def square_sum_of_fibo_last_digit(n):
    last1 = huge_fibonacci(n+1, 10)
    last2 = huge_fibonacci(n, 10)
    return (last1 * last2) % 10
    
def sum_of_fibonacci_naive(n):
    """ return last digit of the sum of first n fibonacci numbers """
    if n<=1:
        return n
    
    previous, current = 0, 1
    sum = previous + current
    # print(0,end=' ')
    # print(1, end=' ')

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        sum %= 10
        # print(sum, end=' ')

    # print()
    return sum 

if __name__ == '__main__':
    # m, n = map(int, input().split())
    n = int(input())
    # sum_of_fibonacci_naive(n)
    # print(sum_of_fibonacci_naive(n))
    # print(sum_of_fibonacci_last_digit(n))
    # print(sum_of_fibonacci_last_digit_1(n))
    # print(sum_of_fibonacci_partial_last_digit(m, n))
    print(square_sum_of_fibo_last_digit(n))
