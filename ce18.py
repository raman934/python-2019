# RG
# 2.8

num = int(input("Enter value of num:\n"))

for i in range(10):
    print(num, end="")
    print(" x ", end="")
    print(i+1, end="")
    print(" = ", end="")
    print(num*(i+1))
