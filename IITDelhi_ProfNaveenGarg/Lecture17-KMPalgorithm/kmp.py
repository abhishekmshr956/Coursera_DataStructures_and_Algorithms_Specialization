def build_lps(pattern):
    length = 0 # length of previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    m = len(text)
    n = len(pattern)

    lps = build_lps(pattern)

    i = 0 # index for text 
    j = 0 # index for pattern

    while i < m:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == n:
            print("Pattern found at index ", i - j)
            j = lps[j - 1]

        elif i < m and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == '__main__':
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    kmp_search(text, pattern)
    # print(build_lps(pattern))