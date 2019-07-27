# RG
# 3.8

N = 5
num = 0

for i in range(N+1):
    for j in range(i):
        if j == 0 or j == i-1:
            print(num, end=' ')
        else :
            print(0, end=' ')
    num += 1
    print('\n')
