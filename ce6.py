# RG
# 1.6

test1 = input("Enter a Letter:\n")

upper = test1.isupper()
lower = test1.islower()

if len(test1) > 1:
    print(" ERROR ! ")
    exit()

if upper is True:
    print("U")

elif lower is True:
    print("L")
