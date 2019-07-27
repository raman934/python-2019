# RG
# 5a.10


def sum_of_arrays(_arr, _arr2):
    n1 = 0
    n2 = 0
    _arr3 = []
    for i in range(len(_arr)):
        n1 += _arr[i]*pow(10, (len(_arr)-i-1))
    for j in range(len(_arr2)):
        n2 += _arr2[j]*pow(10, (len(_arr2)-j-1))
    n3 = n1 + n2
    while n3 != 0:
        _arr3.insert(0, n3 % 10)
        n3 //= 10
    return _arr3


print(sum_of_arrays([1, 0, 2, 9], [3, 4, 5, 6, 7]))
