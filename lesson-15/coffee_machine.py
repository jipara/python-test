from coffe_dictionary import MENU, resources
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def money():
    print("please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_money = ((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies))
    return total_money



def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

Water = (resources["water"])
Milk = (resources["milk"])
Coffee = (resources["coffee"])

is_on = True
while is_on == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"report:\n Water: {Water} ml \n Milk: {Milk} ml \n Coffee: {Coffee} g \n Money: $ {profit} ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment = money()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])
