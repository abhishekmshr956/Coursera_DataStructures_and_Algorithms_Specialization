import argparse
import math

def factors(n):
    factorlist = []
    for i in range(1, n+1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist

def prime(n):
    # return(factors(n) == [1, n])
    return(len(factors(n)) == 2)

def isprime(n):
    if n == 1:
        return False
    result = True
    for i in range(2,n):
        if n % i == 0:
            result = False
            break
    return result

def isprime_while(n):
    if n == 1:
        return False
    result, i = True, 2
    while result and i < n:
        if n % i == 0:
            result = False
        i += 1
    return result

def isprime_while_fast(n):
    if n == 1:
        return False
    result, i = True, 2
    while result and i <= math.sqrt(n):
        if n % i == 0:
            result = False
        i += 1
    return result

# def primelist(n):
#     primelist = []
#     for i in range(1, n+1):
#         if prime(i):
#             primelist.append(i)
#     return primelist

def primesupto(n):
    primelist = []
    for i in range(1, n+1):
        if isprime_while_fast(i):
            primelist.append(i)
    return primelist

def firstprimes(n):
    count, i, pl = 0, 1, []
    while count<n:
        if prime(i):
            pl.append(i)
            count += 1
        i += 1
    return pl

def primediffs(n):
    lastprime = 2
    pd = {} # dictionary for prime differences
    for i in range(3, n+1):
        if isprime_while_fast(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] = pd[d] + 1
            else:
                pd[d] = 1
    return pd

def main():
    parser = argparse.ArgumentParser(description="Specify the number until which you want to find the prime numbers")
    # parser.add_argument('--n', type=int, default=100, help='Specify a number (default is 100)')
    parser.add_argument('n', type=int, help='Specify a number (default is 100)')
    args = parser.parse_args()
    result = primesupto(args.n)
    # result = firstprimes(args.n)
    print(f'Prime numbers from 1 to {args.n}: {result}')

if __name__ == '__main__':
    main()