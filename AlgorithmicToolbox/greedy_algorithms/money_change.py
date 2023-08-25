def change(m):
    return m // 10 + (m % 10) // 5 + ((m % 10) % 5) // 1

if __name__ == '__main__':
    n = int(input())
    print(change(n))