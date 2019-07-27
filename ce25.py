# RG
# 3.2

N = int(input("Enter No. :\n"))

for num in range(2, N):
    temp = 1
    for i in range(2, num):

        if num % i == 0:
            temp = 0

    if temp == 1:
        print(num, end="    ")
