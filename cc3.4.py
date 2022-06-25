"""
-------------------------------------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Code Challenge 3.4: Pizza Order Calculator
Things to learn:
    - Variable, input function, type casting
    - String function: lower()
    - Conditionals: if-else-elif
    - Operator: Assignment, Comparison, Logical[https://www.w3schools.com/python/python_operators.asp]
    - String formatting: string literals
--------------------------------------------------------------------------------------------------------
"""

print('Pizza Order Calculator')
size = input("What size pizza do you want? S(Small), M(Medium), L(Large):\n").lower()
pepperoni = input("Do you want pepperoni? Y(Yes) or N(No):\n").lower()
extra_cheese = input("Do you want extra cheese? Y(Yes) or N(No):\n").lower()

small = 15
medium = 20
large = 25
s_pep = 2
m_pep = 3
cheese = 1

if size == 's':
    if pepperoni == 'y' and extra_cheese == 'y':
        print(f'Your total bill is: {small + s_pep + cheese}')
    elif pepperoni == 'y' and extra_cheese == 'n':
        print(f'Your total bill is: {small + s_pep}')
    elif pepperoni == 'n' and extra_cheese == 'y':
        print(f'Your total bill is: {small + cheese}')
    elif pepperoni == 'n' and extra_cheese == 'n':
        print(f'Your total bill is: {small}')
elif size == 'm':
    if pepperoni == 'y' and extra_cheese == 'y':
        print(f'Your total bill is: {medium + m_pep + cheese}')
    elif pepperoni == 'y' and extra_cheese == 'n':
        print(f'Your total bill is: {medium + m_pep}')
    elif pepperoni == 'n' and extra_cheese == 'y':
        print(f'Your total bill is: {medium + cheese}')
    elif pepperoni == 'n' and extra_cheese == 'n':
        print(f'Your total bill is: {medium}')
elif size == 'l':
    if pepperoni == 'y' and extra_cheese == 'y':
        print(f'Your total bill is: {large + m_pep + cheese}')
    elif pepperoni == 'y' and extra_cheese == 'n':
        print(f'Your total bill is: {large + m_pep}')
    elif pepperoni == 'n' and extra_cheese == 'y':
        print(f'Your total bill is: {large + cheese}')
    elif pepperoni == 'n' and extra_cheese == 'n':
        print(f'Your total bill is: {large}')
