# RG
# 4.9


def armstrong(num):
    temp = num
    res = 0
    while temp > 0:
        res += pow(temp % 10, 3)
        temp //= 10
    if res == num:
        return True
    return False


print(armstrong(370))
