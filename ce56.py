# RG
# 5a.2

arr = [321, 1, 123, 412]
M = int(input("Enter No. :\t"))


def find(_arr, m):
    for i in range(len(_arr)):
        if _arr[i] == m:
            return i
    return -1


print(find(arr, M))
