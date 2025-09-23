# TO calculate the Profti or loss for given selling and cost price
Costprice = float(input("Enter the Cost Price: "))
Sellingprice = float(input("Enter the Selling Price: "))
if Sellingprice > Costprice:
    Profit = Sellingprice - Costprice
    print("You are in Profit of Rs.", Profit)   
elif Costprice > Sellingprice:
    Loss = Costprice - Sellingprice
    print("You are in Loss of Rs.", Loss)
else:
    print("No Profit No Loss")
# End of the program