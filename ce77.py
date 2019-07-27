# RG
# 6.5 # todo learn this method


def toggle_cases(s):
    arr = []
    for i in s:
        if i.isupper():
            arr.append(i.lower())
        else:
            arr.append(i.upper())
    return ''.join(arr)


print(toggle_cases('Hello World'))
