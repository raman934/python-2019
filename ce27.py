# RG
# 3.4

N = int(input("Enter No. :\n"))

even = 0
odd = 0
size = 0
temp = N

while (temp/10) > 0:
    size = size + 1
    temp = temp//10

for i in range(size):
    if i % 2 == 0:
        even += (N % 10)
    else:
        odd += (N % 10)

    N = N//10

print("Sum of even placed digits is %d" % even)
print("Sum of odd placed digit is %d" % odd)
