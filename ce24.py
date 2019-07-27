# RG
# 3.1

N = int(input("Enter No.:\n"))
temp = 1

for i in range(2, N):
    if N % i == 0:
        temp = 0

if temp == 1:
    print("Prime")
else:
    print("Not Prime")
