# RG
# 7.10


def series(n):
    if n == 1:
        return 1
    res = n + series(n-1)
    return res


print(series(30))
