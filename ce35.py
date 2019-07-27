# RG
# 3.12

N = 5
N_new = N // 2

for i in reversed(range(N_new + 1)):

    for j in range(i+1):
        print(" * ", end='')

    for k in range(i, N_new):
        print("   ", end='')

    for l in range(i, N_new):
        print("   ", end='')

    for m in range(i+1):
        print(" * ", end='')

    print("\n")

for i in range(N_new + 1):

    for x in range(i+1):
        print(" * ", end='')

    for y in range(i+1, N_new + 1):
        print("   ", end='')

    for z in range(i, N_new):
        print("   ", end='')

    for w in range(i+1):
        print(" * ", end='')

    print("\n")
