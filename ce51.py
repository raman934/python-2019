# RG
# 4.13


def series(n1, n2):
    i = 0
    j = 0
    while i < n1:
        temp = (3*j)+2
        j += 1
        if temp % n2 != 0:
            print(temp)
            i += 1


series(5, 2)
