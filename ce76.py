# RG
# 6.4 # todo get checked if correct

from ce73 import palindrome_str
from ce75 import return_substrings_str


def count_substring(s):
    arr = []
    n = 0
    arr = return_substrings_str(s)
    for x in arr:
        if palindrome_str(x):
            n += 1
    return n


print(count_substring('Hello World'))
