# RG
# 5a.5


def sort(_arr):
    for i in range(len(_arr)):
        for j in range(i+1, len(_arr)):
            if _arr[i] > _arr[j]:
                temp = _arr[i]
                _arr[i] = _arr[j]
                _arr[j] = temp
    return _arr


print(sort([1, 4, 3, 0, -5, 21]))
