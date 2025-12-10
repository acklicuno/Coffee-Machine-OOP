from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

# Create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on is True:
    print(menu.get_items())  # print items first
    user_choice = input("What would you like to drink?")  # get users option

    # If user wants to turn coffee machine off / If user wants to get report on resources
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()

    drink = menu.find_drink(user_choice)  # Find and assign drink item to variable

    if drink:  # Check if drink has a item
        print("The price of the drink is: ", drink.cost)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
