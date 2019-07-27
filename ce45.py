# RG
# 4.7


def sq_rt(n):
    left = 0
    right = n
    mid = (left + right) / 2
    sq = mid * mid
    while abs(sq - n) > 1e-10:  # given by sir
        if sq < n:
            left = mid
        elif sq > n:
            right = mid
        mid = (left + right) / 2
        sq = mid * mid
    return int(mid)


print(sq_rt(100))
