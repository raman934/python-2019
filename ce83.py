# RG
# 6.11


def permutation_str(s):
    n = len(s)
    fact = 1
    for i in range(n):
        fact *= (i+1)
    while fact > 0:
        temp = n
        for j in range(n):
            print(s[j], end='lol')
            for k in range(n):
                if s[k] != s[j]:
                    print(s[k], end='')
            fact -= 1
            print()


permutation_str('ABCDE')