# RG
# 4.8


def number(n, d):
    res = 0
    while n > 0:
        if n % 10 == d:
            res += 1
        n //= 10
    return res


print(number(31416, 1))
