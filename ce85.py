# RG
# 7.2 #todo learn concept of hcf and lcm


def hcf(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a >= b:
        return hcf(a % b, b)
    elif b > a:
        return hcf(a, b % a)


print(hcf(12, 15))
