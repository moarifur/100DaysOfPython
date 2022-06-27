"""
---------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Code Challenge 3.1: Find 'even' or 'odd'
Things to learn:
    - Variable, input function, type casting
    - conditionals: if, elif and else
    - Modulo Operator
---------------------------------------------------------------------------
"""

print('Check whether the number is given be an even number or an odd number')
number = int(input("Please give me a number to check whether it's an 'even' number or an 'odd' number\n"))
if number % 2 == 0:
    print(f'The given number {number} is an even number')
else:
    print(f'The given number {number} is an odd number')
