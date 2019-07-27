# RG
# 6.3

# S = input("Enter String :\t")


def return_substrings_str(s):
    n = len(s)
    s_new = []
    for i in range(n):
        for j in range(i, n + 1):
            if i < j:
                s_new.append(s[i:j])
    return s_new


# print(return_substrings_str('Hello World'))
