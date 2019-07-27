# RG
# 5a.11
# todo try again


def inverse(n, _arr):
    _arr2 = [None] * n
    for i in range(n):
        _arr2[_arr[i]-1] = i+1
    return _arr2


# print(inverse(5, [5, 4, 1, 2, 3]))
