menu = {"Pizza": 10.00, "Hamburger": 5.00, "Ice Cream": 1.50} #1 - Make a dictionary with items and prices

name = input("What's your name: ") #2 - Ask for name


print("What would you like to order? ('Done' once finished)")
print("Pizza: $10, Hamburger: $5, Ice Cream: $1.50")

total = 0 #3 - Make a total variable

while(True): #4 - Make a while loop that asks the user to enter in an item they want to buy
    order = input("Enter Item: ")
    
    if(order == "Done"):
        break
    elif(order not in menu): #5 - Make sure the item they want to buy is in the menu above or else say it's invalid and rerun the loop
        print("Invalid Order")
        continue
    else:
        total += menu[order] #6 - Add the price of the order (Defined in the dictionary) to the total variable

state = input("Enter State: (az, tx, nv) ") #8 - Ask the user what state they live in and add the respective tax amount to the total
if(state == "az"):
    total = total * (1.056)
elif(state == "tx"):
    total = total * (1.0625)
elif(state == "nv"):
    total = total * (1.046)

try:
    tip = float(input("Tip: ")) #7 - Ask the user to enter a tip amount and add it to the total
except:
    print("Invalid Tip")
    tip = float(input("Tip: "))

total += tip #ad

print("Total: ${}".format(total))
