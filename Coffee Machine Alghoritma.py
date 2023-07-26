from main import MENU

from main import resources
cost2=0
e = MENU["espresso"]
b = e["ingredients"]
espresso_water = b["water"]
espresso_coffee = b["coffee"]
espresso_cost = e["cost"]

l = MENU["latte"]
x = l["ingredients"]
latte_water = x["water"]
latte_milk = x["milk"]
latte_coffee = x["coffee"]
latte_cost = l["cost"]

c = MENU["cappuccino"]
y = c["ingredients"]
cappuccino_water = y["water"]
cappuccino_milk = y["milk"]
cappuccino_coffee = y["coffee"]
cappuccino_cost = c["cost"]
report = resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
while True:
    a = input("Which would you like to cofee ?")
    if a == "off":
        break

    elif a == "report":
        print("water :",water,"\n""milk :",milk,"\n""coffee :",coffee,"\n""cost :",cost2 )

    elif a== "refresh":
        water=resources["water"]
        milk=resources["milk"]
        coffee=resources["coffee"]

    else:
        if a == "espresso":
            if water>=espresso_water and coffee>=espresso_coffee:
                coins=int(input("please pay the cost the espresso (1.5)"))
                if coins < espresso_cost:
                    print("sorry but this money is missing.please you take the remainder of money : ",coins)
                    continue

                else:
                    print("enjoy your meal and this is your remainder of money",coins-espresso_cost)
                    cost2+=espresso_cost
                    water-=espresso_water
                    coffee-=espresso_coffee
                    continue

            else:
                print("sorry but not enough.Please try other coffees")

        elif a == "latte":
            if water >= latte_water and milk>=latte_milk and coffee>=latte_coffee:
                coins = int(input("please pay the coin of latte (2.5)"))
                if coins < latte_cost:
                    print("sorry but money is missing.Please remainder of money")
                    continue

                else:
                    print("enjoy your meal and this is your remainder of money", coins - latte_cost)
                    cost2 += latte_cost
                    water -= latte_water
                    coffee -= latte_coffee
                    continue

            else:
                print("sorry but not enough.Please try other coffees")

        elif a == "cappuccino":
            if water >= cappuccino_water and milk >= cappuccino_milk and coffee >= cappuccino_coffee:
                coins = int(input("please pay the coin of cappucinno (3)"))
                if coins < cappuccino_cost:
                    print("sorry but money is missing.Please remainder of money")
                    continue

                else:
                    print("enjoy your meal and this is your remainder of money", coins - cappuccino_cost)
                    cost2 += cappuccino_cost
                    water -= cappuccino_water
                    milk -= cappuccino_milk
                    coffee -= cappuccino_coffee
                    continue

            else:
                print("sorry but not enough.Please try other coffees")








