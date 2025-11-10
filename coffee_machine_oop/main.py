from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
    
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine = True

while machine:
    options = menu.get_items()
    ans = input(f"What would you like?({options}):")

    if ans == "off":
        machine = False
    elif ans == "report":
            coffee_maker.report()
            money_machine.report()
    else:
        drink = menu.find_drink(ans)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink) 