# RG
# 4.12


def lcm(n1, n2):
    t1 = n1
    t2 = n2
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 = n1-n2
        else:
            n2 = n2-n1
    return (t1 * t2)/(n1 + n2)


print(lcm(12, 15))
