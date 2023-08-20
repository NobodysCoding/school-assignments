#define newVideo and oldVideo
#get user input from totalNew and totalOld
#do the math to get totalPrince
#print results

from decimal import Decimal

newVideo = Decimal('3.00')
oldVideo = Decimal('2.00')
totalNew = int(input("Enter total amount of new videos: "))
totalOld = int(input("Enter total amount of old videos: "))
totalPrice = (newVideo * totalNew) + (oldVideo * totalOld)
print("Your total price is " + "$" + str(totalPrice))
