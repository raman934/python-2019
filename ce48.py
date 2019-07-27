# RG
# 4.10


def print_armstrong(n1, n2):
    for i in range(n1, n2+1):
        temp = i
        res = 0
        while temp > 0:
            res += pow(temp % 10, 3)
            temp //= 10
        if res == i:
            print(i)


print_armstrong(370, 800)
