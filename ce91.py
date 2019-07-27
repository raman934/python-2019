# RG
# 7.8


def pattern_2(n):
    if n == 0:
        return None
    print('* '*n, end='')
    print()
    pattern_2(n-1)


pattern_2(5)
