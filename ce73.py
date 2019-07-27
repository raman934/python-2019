# RG
# 6.1
# todo try again for revision

# S = input("Enter String :\t")


def palindrome_str(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# print(palindrome_str('Hello World'))
