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

item = input('“What would you like? (espresso/latte/cappuccino): ').lower()
ingredients = MENU[item]["ingredients"]


def is_sufficient_money(money):
    noq = int(input('How many quarters?: '))
    nod = int(input('How many dimes?: '))
    non = int(input('How many nickles?: '))
    nop = int(input('How many pennies?: '))
    total = 0.25 * noq + 0.1 * nod + 0.05 * non + 0.01 * nop

    coffee_cost = MENU[item]["cost"]
    if total < coffee_cost:
        print(f'There is not enough money, you need {coffee_cost - total}')
        return
    else:
        print(f'Here is ${total - coffee_cost} in change')


for ingredient in ingredients:
    if ingredient == 'water':
        print(ingredients[ingredient])
    elif ingredient == 'coffee':
        print(ingredients[ingredient])
    elif ingredient == 'milk':
        print(ingredients[ingredient])

is_sufficient_money(item)

# TODO: Code conversion
'''
---------------------------------------------------------------------------
def calculate_resources(item):
    noq = int(input('How many quarters?: '))
    nod = int(input('How many dimes?: '))
    non = int(input('How many nickles?: '))
    nop = int(input('How many pennies?: '))
    total = 0.25 * noq + 0.1 * nod + 0.05 * non + 0.01 * nop

    coffee_cost = data.MENU[item]["cost"]
    if total < coffee_cost:
        print(f'There is not enough money, you need extra ${(coffee_cost - total):.2f}')
        return

---------------------------------------
def is_sufficient_resource(item):
    coffee_type = data.MENU[item]["ingredients"]
    for ingredient in coffee_type:
        if ingredient == 'water':
            print(coffee_type[ingredient])
            if current_resource[ingredient] < coffee_type[ingredient]:
                print(f'There is not enough {ingredient}')
                return
        elif ingredient == 'coffee':
            print(coffee_type[ingredient])
            if current_resource['coffee'] < coffee_type[ingredient]:
                print('There is not enough coffee')
                return
        elif ingredient == 'milk':
            print(coffee_type[ingredient])
            if current_resource['milk'] < coffee_type[ingredient]:
                print('There is not enough milk')
                return
------------------------------------------------------------------------------                
'''
