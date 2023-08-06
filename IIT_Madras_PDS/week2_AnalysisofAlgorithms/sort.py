# O(n^2)
def SelectionSort(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        min_ix = i
        for j in range(i+1, n):
            if l[j] < l[min_ix]:
                min_ix = j
        (l[i], l[min_ix]) = (l[min_ix], l[i])
    return l