# RG
# 4.5
# done in class3 and then improved by Newton's Method


def log(x, n):
    left = 0                      # Newton's Method
    right = x
    mid = (left + right)/2
    logarithm = n ** mid
    while abs(logarithm - x) > 1e-10:
        if logarithm < x:
            left = mid
        else:
            right = mid
        mid = (left + right) / 2
        logarithm = n ** mid
    return mid


print(log(81, 3))
print(log(100, 2))
