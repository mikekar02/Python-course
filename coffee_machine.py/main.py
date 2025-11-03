menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
machine = True
coffee = True


while machine == True:
    ans = input("What would you like? (espresso/latte/cappuccino):").lower() #1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    print(ans)

    if ans != "off": #2 Turn off the Coffee Machine by entering “off” to the prompt.

        if ans == "report":
            print("Water: \n",resources["water"])
            print("Milk: \n",resources["milk"])
            print("Coffee: \n",resources["coffee"])
            print("Money: \n",resources["money"]) #3 Print report

        if ans == "espresso":
            if resources["water"] < menu["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                coffee = False
            elif resources["coffee"] < menu["espresso"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
                coffee = False 

        elif ans == "latte":
            if resources["water"] < menu["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                coffee = False
            elif resources["milk"] < menu["latte"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
                coffee = False
            elif resources["coffee"] < menu["latte"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
                coffee = False 

        elif ans == "cappuccino":
            if resources["water"] < menu["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                coffee = False
            elif resources["milk"] < menu["cappuccino"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
                coffee = False
            elif resources["coffee"] < menu["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
                coffee = False  #4 Check resources sufficient?

        if coffee == True:
            print("Insert coins:")
            one_cents = float(input("1 cents:"))
            five_cents = float(input("5 cents:"))
            ten_cents = float(input("10 cents:"))
            fifteen_cents = float(input("15 cents:"))

            total = (one_cents * 0.01)+(five_cents * 0.05)+(ten_cents * 0.1)+(fifteen_cents * 0.15) #5 Process coins.

            if total >= menu[ans]["cost"]:#6 Check transaction successful?
                change = round(total - menu[ans]["cost"],2)
                if ans == "espresso":
                    resources["water"] = resources["water"] - menu[ans]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - menu[ans]["ingredients"]["coffee"]
                    print("Here is",change,"in change.")
                    print("Here is your latte enjoy!")
                else:
                    resources["water"] = resources["water"] - menu[ans]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - menu[ans]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - menu[ans]["ingredients"]["coffee"]#7 Make Coffee.
                    print("Here is",change,"in change.")
                    print("Here is your latte enjoy!")
            else:
                print("“Sorry that's not enough money. Money refunded.")





