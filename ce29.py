# RG
# 3.6

N = int(input("Enter value of N :\n"))
num1 = 0
num2 = 1
num = 0
i = 2

while i <= N:
    num = num1 + num2
    num1 = num2
    num2 = num
    i += 1
    if i == N:
        print(num)
