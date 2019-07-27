# RG
# 4.6


def sqr_rt(n):
    left = 0
    right = n
    mid = (left + right)/2
    sq = mid*mid
    while abs(sq - n) > 1e-10:
        if sq < n:
            left = mid
        else:
            right = mid
        mid = (left + right)/2
        sq = mid*mid
    return mid


print(sqr_rt(9))
