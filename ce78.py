# RG
# 6.6 # todo learn


def ascii_change(s):
    n = len(s)
    arr = ['']*n
    for i in range(n):
        if (i+1) % 2 == 0:
            x = ord(s[i]) - 1
        else:
            x = ord(s[i]) + 1
        arr[i] = chr(x)
    return str(''.join(arr))


print(ascii_change('Hello World'))
