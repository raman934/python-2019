# RG
# 6.7 # todo took a lotta time, try again!

# S = input()


def ascii_diff(s):
    n = len(s)
    arr = []
    for i in range(n):
        arr.append(s[i])
        if i < n-1:
            j = ord(s[i+1])-ord(s[i])
        else:
            break
        x = '\t{}\n'.format(j)
        arr.append(x)
    return str(''.join(arr))


print(ascii_diff('Hello World'))
