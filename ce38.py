# RG
# 3.15

N = 4
num = 0

for i in range(N+1):

    for j in range(i):
        num += 1
        print(num, end='  ')

    for k in range(i, N):
        print("   ", end='')

    for l in range(i, N-1):
        print("   ", end='')

    for m in range(i):
        if i != N:
            num -= 1
            print(num+1, end='  ')
        else:
            if m != N-1:
                num -= 1
                print(num, end='  ')

    print("\n")
