# RG
# 7.3 # todo learn


def is_palindrome(s):
    n = len(s)
    if n == 1:
        return True
    elif s[0] == s[n - 1] and is_palindrome(s[1:n - 1]):
        return True
    return False


print(is_palindrome('level'))
