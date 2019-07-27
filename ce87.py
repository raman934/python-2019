# RG
# 7.4


def reverse(arr):
    n = len(arr)
    x = []
    if len(arr) == 0:
        return []
    else:
        for i in range(n):
            x.append(arr[-1])
            x[1:n-1] = reverse(arr[:-1])
            return x


print(reverse([1, 'Hello', 3, 4, 5]))
