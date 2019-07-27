# RG
# 5b.2
# todo something about that last COMMA

arr = [[(j*10)+i for i in range(1, 5)] for j in range(1, 5)]
# for i in range(4):
#     for j in range(4):
#         arr[i][j] = input()

n = len(arr)
for x in range(n):
    for y in range(n):
        print(arr[y][x], end=', ')
