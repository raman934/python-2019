# RG
# 7.1


def fact(n):
    if n > 1:
        return n*fact(n-1)
    elif n < 0:
        return n*fact(n+1)
    return 1


print(fact(5))
