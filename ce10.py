# RG
# 1.10

print("Print valid sides for a Triangle\n")
side1 = int(input("Enter side 1 of triangle:\n"))
side2 = int(input("Enter side 2 of triangle:\n"))
side3 = int(input("Enter side 3 of triangle:\n"))

if side1==side2==side3:
    print("Triangle is equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")