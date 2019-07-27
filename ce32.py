# RG
# 3.9

N = 6
num = 0
num2 = 3
j = 0
num3 = 0

for i in range(N+1):
    temp = 0
    for j in range(i):
        if j == 0 or j == i-1:
            print(1, end=' ')
        elif j == 1 or j == i-2:
            print(num-1, end=' ')
        else:
            if temp == 0:
                num3 += num - 2
                temp = 1
            print(num3+num2, end=' ')
    num += 1
    print('\n')
