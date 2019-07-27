# RG
# 6.8

# S = input()


def count_char(s):
    n = len(s)
    arr = []
    x = 0
    y = ''
    for i in range(n):
        arr.append(s[i])
    for j in range(n):
        if arr.count(arr[j]) > x:
            y = arr[j]
            x = arr.count(arr[j])
    return y


print(count_char('Hello World'))
