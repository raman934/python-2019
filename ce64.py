# RG
# 5a.9


def triplets(_arr, target):
    _arr = sorted(_arr)
    for i in range(len(_arr)):
        for j in range(i + 1, len(_arr)):
            for k in range(j + 1, len(_arr)):
                if _arr[i] + _arr[j] + _arr[k] == target:
                    print(end='(')
                    print(_arr[i], end=', ')
                    print(_arr[j], end=', ')
                    print(_arr[k], end=')\n')


triplets([3, 1, 9, 7, 5, -1], 9)
