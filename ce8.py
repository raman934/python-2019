# RG
# 1.8

money = int(input("Enter total amount of money(Rs.):\n"))

notes_2000 = int(money/2000)
notes_500 = int((money-2000*notes_2000)/500)
notes_100 = int((money-2000*notes_2000-500*notes_500)/100)
notes_50 = int((money-2000*notes_2000-500*notes_500-100*notes_100)/50)

print("You need :\n")
print("{} note(s) of 2000 \n".format(notes_2000))
print("{} note(s) of 500 \n".format(notes_500))
print("{} note(s) of 100 \n".format(notes_100))
print("{} note(s) of 50 \n".format(notes_50))
