# RG
# 3.10

N = 4
num = 0
num1 = 0
num2 = 1
temp = 1

for i in range(N+1):
    for j in range(i):
        print(num, end=' ')
        if temp == 1:
            num = 1
            temp = 0
        else:
            num = num1 + num2
            num1 = num2
            num2 = num
    print('\n')
