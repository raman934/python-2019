# RG
# 7.16

# arr = [1, 2, 3]

#
# start = 0
# end = 3
#
# while start < end:
#     print(arr[start:], end='     ')
#     arr.append(arr[start])
#     start += 1
# start = 0
# while start >= 0:
#     print(arr[start:], end='     ')
#     arr.append(arr[end])
#     start -= 1
#     end -= 1


def permutation(arr):
    n = len(arr)
    j = 0
    res = []
    for i in range(n):
        res.append(arr[i:])
        arr.append(arr[j])
        j += 1
        print(res[i])
    # return permutation()


permutation([1, 2, 3])
