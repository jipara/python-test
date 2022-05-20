from coffe_dictionary import resources, MENU

def user_choice():
  user_choice = (input("what would you like? (espresso/latte/cappuccino): \n")).lower

  return user_choice


choice = user_choice()


print("Please insert coins.")

latte_money = MENU["latte"]["cost"]
espresso_money = MENU["espresso"]["cost"]
cappuccino_money = MENU["cappuccino"]["cost"]


def money():
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_money = ((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies))
    return total_money

total_money = money()

def money_difference(money_from_customer, coffee_money):
    change = round(total_money - coffee_money, 2)
    if change < coffee_money:
        print("Sorry that's not enough money. Money refunded.")
    elif change >= coffee_money:
        print(f"your change is: {change}")
        return change


money_difference(total_money, latte_money)






Water = (resources["water"])


Milk = (resources["milk"])


Coffee = (resources["coffee"])


print(f"report:\n Water: {Water} \n Milk: {Milk} \n Coffee: {Coffee} ")





def ingredients(choice1):
    water = (resources["water"])
    print(water)
    if choice == "espresso":
        new_water = water - MENU["espresso"]["ingredients"]["water"]
        print(new_water)
        #return new_water
    elif choice == "latte":
        new_water = water - MENU["latte"]["ingredients"]["water"]
        print(new_water)
        #return new_water
    elif choice == "cappuccino":
        new_water = water - MENU["cappuccino"]["ingredients"]["water"]
        print(new_water)
        #return new_water

print(ingredients(choice))

    #resource_water_espresso = (water - MENU["espresso"]["ingredients"]["water"])
    #resource_water_latte = (water - MENU["latte"]["ingredients"]["water"])
    #resource_water_cappuccino = (water - MENU["cappuccino"]["ingredients"]["water"])


#def report(total):

