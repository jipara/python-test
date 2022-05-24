from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True
coffee_maker.report()
money_machine.report()

print(coffee_maker)
print(money_machine)

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        print("Sorry we are close for maintenance ")
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
