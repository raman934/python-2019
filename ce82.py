# RG
# 6.10

# S = input()


def remove_repeat(s):
    n = len(s)
    arr = [s[i] for i in range(n)]
    j = 1
    while j < n:
        if arr[j] == arr[j-1]:
            temp = '{}'.format(arr.count(arr[j]))
            while arr.count(arr[j]) >= 2 and (arr[j] == arr[j-1] or arr[j] == arr[j+1]):
                arr.pop(j)
                n -= 1
                if arr.count(arr[j-1]) == 1:
                    break
            arr.insert(j, temp)
            n += 1
        j += 1
    return str(''.join(arr))


print(remove_repeat('aaabbccds'))
