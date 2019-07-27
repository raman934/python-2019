# RG
# 2.9

num = int(input("Enter No.:\n"))
temp = 1

for i in range(2, num):
    if num % i == 0:
        temp = 0

if temp == 1:
    print("Prime")
else:
    print("Not Prime")
