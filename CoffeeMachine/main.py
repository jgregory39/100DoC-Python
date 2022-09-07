MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0.0
}


# Generate a report about current resources
def report():
    # Get resources and append units
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    return


# Check if resources are sufficient to make a drink
def check_resources(drink):
    can_make = True
    requirement = MENU[drink]["ingredients"]
    if requirement["water"] > resources["water"]:
        can_make = False
        print("Sorry, there is not enough water")
    if requirement["milk"] > resources["milk"]:
        can_make = False
        print("Sorry, there is not enough milk")
    if requirement["coffee"] > resources["coffee"]:
        can_make = False
        print("Sorry, there is not enough coffee")
    return can_make


# Accept coins and return total value
def take_coins():
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


# Check transactional success
def transaction(funds, drink):
    cost = MENU[drink]["cost"]
    if cost < funds:
        change = funds - cost
        resources["money"] += cost
        print(f"Here is ${change} dollars in change.")
    elif cost == funds:
        resources["money"] += cost
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    return True


# Make coffee by removing appropriate resources from count.
def coffee(drink):
    requirements = MENU[drink]["ingredients"]
    resources["water"] -= requirements["water"]
    resources["milk"] -= requirements["milk"]
    resources["coffee"] -= requirements["coffee"]
    print(f"Here is your {drink}. Enjoy!")
    return

while True:
    response = input("What would you like? (espresso/latte/cappuccino):")
    if response == "off":
        break
    elif response == "report":
        report()
    elif response != "espresso" and response != "latte" and response != "cappuccino":
        print("Invalid response. Please try again.")
    elif check_resources(response):  # Only executes if resources are available
        funds = take_coins()
        if transaction(funds, response):
            coffee(response)