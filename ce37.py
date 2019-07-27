# RG
# 3.14

N = 3
N_new = (N + 1) // 2
num = 0

for i in reversed(range(N_new + 1)):

    for j in range(i):
        print("   ", end='')

    for k in range(i, N_new + 1):
        num += 1
        print(num, end='  ')

    for l in range(i, N_new):
        num -= 1
        print(num, end='  ')

    print("\n")

for i in range(N_new + 1):

    for x in range(i+1):
        print("   ", end='')

    for y in range(i+1, N_new):
        num += 1
        print(num, end='  ')

    for z in range(i+1, N_new + 1):
        num -= 1
        print(num, end='  ')

    print("\n")
