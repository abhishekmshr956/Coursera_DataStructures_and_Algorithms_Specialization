# O(n)
def naivesearch(v, l):
    for x in l:
        if v == x:
            return True
    return False

# O(log n)
def binarysearch(v, l):
    if l == []:
        return False
    
    m = len(l) // 2

    if v == l[m]:
        return True
    
    if v < l[m]:
        return binarysearch(v, l[:m])
    else:
        return binarysearch(v,l[m+1:])
    
import numpy as np
def StressTest(f1, f2=naivesearch):
    np.random.seed(42)
    while True:
        l = np.random.randint(-30, 30, (30,))
        l = np.sort(l).tolist()
        v = np.random.randint(-100, 100)
        # print(v, l)
        result1 = f1(v, l)
        # print(result1)
        result2 = f2(v, l)
        if result1 == result2:
            print("OK")
        else:
            print(f"Wrong answer: {v = }, {l = }, {result1 = }, {result2 = }")
            break