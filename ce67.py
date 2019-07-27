# RG
# 5a.12

from ce66 import inverse


def mirror_inverse(n, _array):
    x = inverse(n, _array)
    if x == _array:
        return True
    else:
        return False


print(mirror_inverse(5, [1, 2, 3, 4, 5]))
