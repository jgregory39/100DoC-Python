from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu = Menu()
vendor = MoneyMachine()

while True:
    order = input(f"What would you like? ({menu.get_items()}):")
    if order.__eq__("off"):
        break
    elif order.__eq__("report"):
        maker.report()
        vendor.report()
    elif menu.find_drink(order):
        drink = menu.find_drink(order)
        if maker.is_resource_sufficient(drink) and vendor.make_payment(drink.cost):
            maker.make_coffee(drink)



