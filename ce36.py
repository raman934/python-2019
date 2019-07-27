# RG
# 3.13

N = 4
num = 0

for i in reversed(range(N)):

    for j in range(i):
        print("   ", end='')

    for k in range(i, N):
        num += 1
        print(num, end='  ')

    for l in range(i, N-1):
        num -= 1
        print(num, end='  ')

    print("\n")
