# RG
# 3.5

N = int(input("Enter value of N :\n"))
num1 = 0
num2 = 1
print(num1, end='  ')
print(num2, end='  ')
num = 0

while (num1 + num2) < N:
    num = num1 + num2
    print(num, end='  ')
    num1 = num2
    num2 = num
