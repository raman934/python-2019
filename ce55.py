# RG
# 5a.1

arr = []
N = int(input())
for i in range(N):
    arr.append(int(input("Enter %d element:\t" % (i + 1))))


def max_val(_list, n):
    temp = 0
    for x in range(n):
        if _list[x] > temp:
            temp = _list[x]
    return temp


print(max_val(arr, N))
