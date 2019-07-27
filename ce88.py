# RG
# 7.5
# although I did it by myself but still, learn this method


def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a, -b)
    x = power(a, b // 2)
    if b % 2 == 0:
        return x * x
    else:
        return a * x * x


print(power(2, 5))
