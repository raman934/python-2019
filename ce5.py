# RG
# 1.5

year = int(input())

if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap")
else:
    print("Not Leap")
