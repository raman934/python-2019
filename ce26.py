# RG
# 3.3

N = int(input("Enter No. :\n"))
res = 0
size = 0
temp = N

while (temp/10) > 0:
    size = size + 1
    temp = temp//10

for i in range(size):
    res += (N % 10) * (pow(10, size - i - 1))
    N = N//10

print("Result is %d" % res)
