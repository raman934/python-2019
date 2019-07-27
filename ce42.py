# RG
# 4.4


def prime(n):
    boo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            boo = False
            break
    return boo


n = int(input("Enter:\t"))

print(prime(n))