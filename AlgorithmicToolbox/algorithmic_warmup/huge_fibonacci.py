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
    
if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    # print(find_pisano_period(input_m))
    print(huge_fibonacci(input_n, input_m))