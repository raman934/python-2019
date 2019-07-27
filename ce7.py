# RG
# 1.7

month = int(input("Enter Month:\n"))

if 1 <= month <= 7:
    if month == 2:
        print("28 days")
    elif month%2==0:
        print("30 days")
    else:
        print("31 days")

elif 8 <= month <= 12:
    if month%2==0:
        print("31 days")
    else:
        print("30 days")
else:
    print("Error !\nEnter a no. between 1 and 12(inclusive)")