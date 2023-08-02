import argparse

def gcd(m,n):
    cf = []
    for i in range(1, min(m,n) + 1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
    return cf[-1]

def gcd_mrcf(m,n):
    for i in range(1, min(m,n) + 1):
        if m%i == 0 and n%i == 0:
            mrcf = i
    return mrcf

def gcd_diff_recur(m,n):
    a, b = max(m,n), min(m,n)
    if a % b == 0:
        return b
    else:
        return gcd_diff_recur(b, a - b)
    
def gcd_fast(m,n):
    """finds gcd using Euclid's algorithm"""
    a, b = max(m,n), min(m,n)
    if a % b == 0:
        return b
    else:
        return gcd_diff_recur(b, a % b)
    
def gcd_fast_1(m,n):
    if n == 0:
        return m
    else:
        return gcd_fast(n, m % n)
    


def main():
    parser = argparse.ArgumentParser(description="Enter two numbers to find the gcd of")
    parser.add_argument('m', type=int, help='First number')
    parser.add_argument('n', type=int, help='Second number')
    args = parser.parse_args()
    print(gcd_fast(args.m, args.n))

if __name__=='__main__':
    main()