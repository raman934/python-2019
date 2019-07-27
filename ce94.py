# RG
# 7.11


def sort(_arr):
    n = len(_arr)
    left = 0
    right = n - 1
    if left + 1 >= right:
        if _arr[left] <= _arr[right]:
            return True
        else:
            return False
    if _arr[left] < _arr[right]:
        return sort(_arr[1:n])
    else:
        return False


print(sort([1, 2, 3, 4, 5, 7]))
