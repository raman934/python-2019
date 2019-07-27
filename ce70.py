# RG
# 5b.3
# todo something about that last COMMA

arr = [[(j*10)+i for i in range(1, 5)] for j in range(1, 5)]
# for i in range(4):
#     for j in range(4):
#         arr[i][j] = input()

z = 0
n = len(arr)
for x in range(n*2):
    if z == 0:
        for y in range(n):
            print(arr[y][x], end=', ')
            temp = y
    elif z == 1:
        for y in range(z, n):
            print(arr[temp][y], end=', ')
            temp2 = y
    elif z == 2:
        for y in range(z - 1, n):
            print(arr[n - y - 1][temp2], end=', ')
            temp = n - y - 1
    elif z == 3:
        for y in range(z - 1, n):
            print(arr[temp][n - y], end=', ')
            temp2 = n - y
    elif z == 4:
        for y in range(z - 2, n):
            print(arr[y - 1][temp2], end=', ')
            temp = y - 1
    elif z == 5:
        for y in range(z - 2, n):
            print(arr[temp][y - 1], end=', ')
            temp2 = y - 1
    elif z == 6:
        for y in range(z - 3, n):
            print(arr[y - 2][temp2], end=', ')
    z += 1
