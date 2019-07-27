# RG
# 6.9

# S = input()


def remove_duplicates(s):
    n = len(s)
    arr2 = [s[i] for i in range(n-1) if s[i] != s[i+1] or i == n-1]
    if s[n-2] != s[n-1]:
        arr2.append(s[n-1])
        return str(''.join(arr2))


print(remove_duplicates('aabccba'))
