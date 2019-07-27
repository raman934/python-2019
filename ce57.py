# RG
# 5a.3

M = int(input("Enter No. :\t"))
arr = []
for d in range(1024):
    arr.append(d)


def find(_arr, m):
    x = 0
    left = 0
    right = len(_arr)
    mid = (left + right) // 2
    element = _arr[mid]
    while element != m:
        if element < m:
            x += 1
            left = mid
        else:
            x += 1
            right = mid
        mid = (left + right) // 2
        element = _arr[mid]
    for i in range(left, right):
        if _arr[i] == m:
            x += 1
            # print(x, end=' lol\n')            to check the no. of times comparison occurs
            return i
    return -1


print(find(arr, M))
