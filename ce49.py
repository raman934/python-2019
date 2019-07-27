# RG
# 4.11
# todo do again


def hcf(n1, n2):            # Euclid's Method
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 = n1-n2
        else:
            n2 = n2-n1
    return n1 + n2


print(hcf(12, 15))
