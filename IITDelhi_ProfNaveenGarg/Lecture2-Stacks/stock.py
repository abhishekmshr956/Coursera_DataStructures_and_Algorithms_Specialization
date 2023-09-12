"""
The span s_i of a stock's price on a certain day i is the maximum number of consecutive days (up to the current day) 
the price of the stock has been less than or equal to its price on day i.
Input: the stock prices P as an array of numbers
Output: the span array S where S[i] is the span for the ith day
"""
from stack import Stack

def computeSpans1(P):
    """ start from i position. keep going back until find a higher stock price
    O(n^2)
    """
    S = [None] * len(P)
    for i in range(len(P)):
        k = 0
        done = False
        while k != i+1 and done == False:
            if P[i - k] <= P[i]:
                k += 1
            else:
                done = True
        S[i] = k
    return S

def computeSpans2(P):
    """ more efficient algorithm """
    S = [None] * len(P)
    D = Stack()
    for i in range(len(P)):
        done = False
        while not D.isEmpty() and done == False:
            if P[i] < P[D.top()]:
                h = D.top()
                done = True
            else:
                D.pop()
        if D.isEmpty():
            h = -1
        D.push(i)
        S[i] = i - h
    return S

import numpy as np
if __name__ == '__main__':
    # P = [10, 8, 3, 4, 3, 7, 9]
    # P = [1, 2]
    np.random.seed(42)
    P = np.random.randint(0, 15, 6)
    print(P)
    print(computeSpans1(P))
    print(computeSpans2(P))