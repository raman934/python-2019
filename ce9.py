# RG
# 1.9

side1 = int(input("Enter side 1 of triangle:\n"))
side2 = int(input("Enter side 2 of triangle:\n"))
side3 = int(input("Enter side 3 of triangle:\n"))

if side1+side2>=side3 and side1+side3>=side2 and side2+side3>=side1:
    print("Triangle can be formed")
else:
    print("Triangle can not be formed")