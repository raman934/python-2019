# RG
# 5a.8


def pairs(_arr, target):
    _arr = sorted(_arr)
    for i in range(len(_arr)):
        for j in range(i+1, len(_arr)):
            if _arr[i] + _arr[j] == target:
                print(_arr[i], end=' and ')
                print(_arr[j])


pairs([3, 1, 9, 7, 5, -1], 8)
