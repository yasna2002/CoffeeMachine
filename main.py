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
    "money": 0,
}


def print_report():
    for resource in resources:
        print(f"{resource.capitalize()}: {resources[resource]}")


def enough_resources(user_input):
    for resource in resources:
        if resource == 'money':
            break
        if user_input == 'espresso':
            if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                return False
            elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
                return False
        else:
            if resources[resource] < MENU[user_input]["ingredients"][resource]:
                print(f"Sorry there is not enough {resource}.")
                return False
    return True


def process_coins(coffee_price, user_input):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    user_payment = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if user_payment < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is {round((user_payment - coffee_price), 2)} in change.")
        resources["money"] += coffee_price
        print(f"Here is your {user_input} ☕ Enjoy!")
        return True


while 1:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'espresso':
        if not enough_resources(user_input):
            continue
        if not process_coins(MENU["espresso"]["cost"], user_input):
            continue
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif user_input == 'latte':
        if not enough_resources(user_input):
            continue
        if not process_coins(MENU["latte"]["cost"], user_input):
            continue
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif user_input == 'cappuccino':
        if not enough_resources(user_input):
            continue
        if not process_coins(MENU["cappuccino"]["cost"], user_input):
            continue
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    elif user_input == 'report':
        print_report()
    elif user_input == 'off':
        break


