"""
-------------------------------------------------------------------------
Day15: Local Development Environment Setup & the Coffee Machine[Intermediate]
Project15: Coffee Machine Program
Code Overview: https://tinyurl.com/22cut5pr
Code Preview: https://replit.com/@appbrewery/coffee-machine-final
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
"""

import data

current_resource = {
    'water': 500,
    'milk': 100,
    'coffee': 50,
    'money': 0
}


# TODO-03: Print the current resource values.
def generate_report():
    print(f"Water: {current_resource['water']}")
    print(f"Milk: {current_resource['milk']}")
    print(f"Coffee: {current_resource['coffee']}")
    print(f"Money: {current_resource['money']}")


# TODO-04: Check resources sufficient?
def is_sufficient_resource(item):
    coffee_type = data.MENU[item]["ingredients"]
    for ingredient in coffee_type:
        if current_resource[ingredient] < coffee_type[ingredient]:
            print(f'There is not enough {ingredient}')
            return 'not_enough'


# TODO-05: Process coins: If there are sufficient resources to make
#  the drink selected, then the program should prompt the user to insert coins
def calculate_resources(item):
    noq = int(input('How many quarters?: '))
    nod = int(input('How many dimes?: '))
    non = int(input('How many nickles?: '))
    nop = int(input('How many pennies?: '))
    total = 0.25 * noq + 0.1 * nod + 0.05 * non + 0.01 * nop
    coffee_cost = data.MENU[item]["cost"]

    # TODO-06: Check transaction successful?
    # TODO-07: Make Coffee.
    if total < coffee_cost:
        print(f'There is not enough money, you need extra ${(coffee_cost - total):.2f}')
        return
    else:
        print(f'Here is ${(total - coffee_cost):.2f} in change')
        print(f'Here is your {item} ☕️Enjoy!')
        current_resource['money'] += data.MENU[item]["cost"]
        current_resource['water'] -= data.MENU[item]['ingredients']["water"]
        current_resource['coffee'] -= data.MENU[item]['ingredients']["coffee"]
        if item != 'espresso':
            current_resource['milk'] -= data.MENU[item]['ingredients']["milk"]


# TODO-02: Turn off the Coffee Machine by entering “off” to the prompt.
is_turn_off = False

while not is_turn_off:
    # TODO-01: Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    choice = input('“What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'espresso':
        if is_sufficient_resource(choice) != 'not_enough':
            calculate_resources(choice)
    elif choice == 'latte':
        if is_sufficient_resource(choice) != 'not_enough':
            calculate_resources(choice)
    elif choice == 'cappuccino':
        if is_sufficient_resource(choice) != 'not_enough':
            calculate_resources(choice)
    elif choice == 'report':
        generate_report()
    elif choice == 'off':
        is_turn_off = True
