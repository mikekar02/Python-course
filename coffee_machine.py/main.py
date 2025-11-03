MENU = {
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

    if ans != "off": #2 Turn off the Coffee Machine by entering “off” to the prompt.

        if ans == "report":
            print("Water: \n",resources["water"])
            print("Milk: \n",resources["milk"])
            print("Coffee: \n",resources["coffee"])
            print("Money: \n",resources["money"]) #3 Print report

    if ans == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            coffee = False
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            coffee = False
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            coffee = False #4 Check resources sufficient?



#5 Process coins.
#6 Check transaction successful?
#7 Make Coffee.
