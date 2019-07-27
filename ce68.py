# RG
# 5b.1
# todo done that last COMMA

arr = [[(j*10)+i for i in range(1, 5)] for j in range(1, 5)]
# for i in range(4):
#     for j in range(4):
#         arr[i][j] = input()

z = 2
for x in arr:
    if z % 2 == 0:
        for y in x:
            print(y, end=', ')
    else:
        for y in reversed(x):
            if x == arr[len(arr)-1] and y == x[0]:
                print(y, end='')
            else:
                print(y, end=', ')
    z += 1
