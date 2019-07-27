# RG
# 5a.7(ii)


def intersection(_arr, _arr2):
    _arr = sorted(_arr)
    _arr2 = sorted(_arr2)
    _arr3 = []
    strlen = len(_arr)
    strlen2 = len(_arr2)
    for i in range(strlen):
        for j in range(strlen2):
            if _arr[i] == _arr2[j]:
                _arr3.append(_arr[i])
                break
    print(_arr3)


intersection([1, 2, 3, 1, 2, 4, 1], [2, 1, 3, 1, 5, 2, 2])
