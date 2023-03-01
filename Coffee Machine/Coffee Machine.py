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
}

def put_money():
    quarters = float(input("How many Quarters?: ")) * 0.25
    dimes = float(input("How many Dimes?: ")) * 0.1
    nickles = float(input("How many Nickles?: ")) * 0.05
    pennies = float(input("How many Pennies?: ")) * 0.01
    money = quarters + dimes + nickles + pennies
    return money


def what_coffee(type):
    print(f"Costs {MENU[type]['cost']} Euros")
    money = float(put_money())
    change = money - MENU[type]["cost"]
    profit = []
    profit.append(MENU[type]["cost"])
    print(profit)
    print(f"Your change is {change}")


def rem_wat(type):
    rem_water = float(resources["water"] - MENU[type]["ingredients"]["water"])
    return rem_water


def rem_mil(type):
    rem_milk = float(resources["milk"] - MENU[type]["ingredients"]["milk"])
    print(rem_milk)
    return rem_milk

def rem_cof(type):
    rem_coffee = float(resources["coffee"] - MENU[type]["ingredients"]["coffee"])
    print(rem_coffee)
    return rem_coffee

yes = True
while yes:
    customer = input("Would you like a coffee or a report?\n").lower()
    count_wat = 0.0
    if customer == "coffee" or customer == "cafe" or customer == "caffe":
        choice = input("What coffee would you like?\n 1.Espresso\n 2.Latte\n 3.Cappuccino \n")
        if choice == "1":
            what_coffee("espresso")
            count_wat -= float(rem_wat("espresso"))
            print(count_wat)
        elif choice == "2":
            what_coffee("latte")

        elif choice == "3":
            what_coffee("cappuccino")

    elif customer == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    else:
        yes = False




