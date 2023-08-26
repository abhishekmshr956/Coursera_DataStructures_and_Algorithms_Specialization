from sys import stdin

def max_ad(n, profits, clicks):
    value = 0
    for i in range(n):
        p_max_i = max(profits)
        profits.remove(p_max_i)
        clicks_max_i = max(clicks)
        clicks.remove(clicks_max_i)
        value += p_max_i * clicks_max_i
    return value


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n = data[0]
    profits = data[1:n+1]
    clicks = data[n+1:]
    print(max_ad(n, profits, clicks))

