# RG
# 5a.4

arr = [1, 2, 3, 4, 5]


def reverse(_arr):
    _arr2 = []
    for i in reversed(range(len(_arr))):
        _arr2.append(_arr[i])
    return _arr2


print(reverse(arr))
