# RG
# 6.2 # todo try to make it more efficient

# S = input("Enter String :\t")


def substrings_str(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n + 1):
            if i < j:
                s_new = s[i:j]
                print(s_new)


substrings_str('Hello World')
