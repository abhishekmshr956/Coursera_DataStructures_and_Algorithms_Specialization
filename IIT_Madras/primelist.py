import argparse

def factors(n):
    factorlist = []
    for i in range(1, n+1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist

def prime(n):
    # return(factors(n) == [1, n])
    return(len(factors(n)) == 2)

def primelist(n):
    primelist = []
    for i in range(1, n+1):
        if prime(i):
            primelist.append(i)
    return primelist

def main():
    parser = argparse.ArgumentParser(description="Specify the number until which you want to find the prime numbers")
    # parser.add_argument('--n', type=int, default=100, help='Specify a number (default is 100)')
    parser.add_argument('n', type=int, help='Specify a number (default is 100)')
    args = parser.parse_args()
    result = primelist(args.n)
    print(f'Prime numbers from 1 to {args.n}: {result}')

if __name__ == '__main__':
    main()