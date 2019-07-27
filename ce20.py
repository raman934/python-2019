# RG
# 2.10

for num in range(2, 100):
    temp = 1
    for i in range(2, num):

        if num % i == 0:
            temp = 0

    if temp == 1:
        print(num, end="    ")
