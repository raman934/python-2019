# RG
# 3.7

N = 4
num = 1

for i in range(N+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print('\n')
