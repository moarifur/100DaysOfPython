"""
---------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Code Challenge 3.3: Leap Year Calculator
Things to learn:
    - Variable, input function, type casting
    - conditionals: if-else
    - Modulo Operator
    - String formatting: string literals
---------------------------------------------------------------------------
"""

print('Leap Year Calculator')
year = int(input("Type a year to check whether it's a leap year or not:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The year is given {year}, is a leap year!')
        else:
            print(f'The year is given {year}, is not a leap year!')
    else:
        print(f'The year is given {year}, is a leap year!')
else:
    print(f'The year is given {year}, is not a leap year!')
