"""
-------------------------------------------------------------------------
Day10: Functions with Outputs
Project10: Pythonista - A Calculator App
Code Overview:
Code Preview: https://replit.com/@appbrewery/calculator-final
*** Press 'Run'/ 'play' button to understand how does the challenge work
--------------------------------------------------------------------------
TODO:

"""

import os
from art import logo

# Print logo
print(logo)


def new_clac():
    os.system('cls')
    print(logo)


def calc_operation(f_number, s_number, op):
    result = 0

    if op == '/' and s_number == 0:
        return 'Undefined!'

    if op == '+':
        result = f_number + s_number
    elif op == '-':
        result = f_number - s_number
    if op == '*':
        result = f_number * s_number
    elif op == '/':
        result = f_number / s_number

    # print(f"{f_number} {op} {s_number} = {result}")
    return result


first_number = float(input('Enter First Number: '))
while True:
    operator_list = '''
    +
    -
    *
    /
    '''
    print(operator_list)
    operator = input('Pick an operation: ')
    second_number = float(input('Enter Second Number: '))

    output = calc_operation(first_number, second_number, operator)
    print(f"{first_number} {operator} {second_number} = {output}")

    decision = input(f"Type 'y' to continue calculating with {output},"
                     " or type 'n' to start a new calculation"
                     " or type 'exit' end the program: ")
    if decision == 'y':
        first_number = calc_operation(first_number, second_number, operator)
    elif decision == 'n':
        new_clac()
    elif decision == 'exit':
        break

"""
------------------------------------------------------------------------------
Things you'll learn:
    - User defined function: new_clac(), calc_operation(f_number, s_number, op)
    - Conditional: if-else
    - Iteration: for-in loop in dictionary, infinite while loop with break    
    - Module: os, art(user defined)
    - os method: os.system('cls') - for clearing screen in console
---------------------------------------------------------------------------------  
"""
