import argparse

def gcd(m,n):
    cf = []
    for i in range(1, min(m,n) + 1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
    return(cf[-1])

def main():
    parser = argparse.ArgumentParser(description="Enter two numbers to find the gcd of")
    parser.add_argument('m', type=int, help='First number')
    parser.add_argument('n', type=int, help='Second number')
    args = parser.parse_args()
    print(gcd(args.m, args.n))

if __name__=='__main__':
    main()