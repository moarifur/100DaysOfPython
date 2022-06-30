"""
--------------------------------------------------------------------------------------------
Day08: Function Parameters & Caesar Cipher[Beginner]
Code Challenge 8.1: Paint Area Calculator
Code Overview: https://replit.com/@appbrewery/day-8-1-exercise#README.md
Code Preview: https://repl.it/@appbrewery/day-8-1-solution
*** Press 'Run'/ 'play' button to understand how does the challenge work
Things to learn:
    - Module: math module
    - math method: ceil()
    - Create function
-----------------------------------------------------------------------------------------------
"""
import math

print('Paint Area Calculator')

height = int(input('Please enter the height of the wall in meter: '))
width = int(input('Please enter the width of the wall in meter: '))
coverage = 5


def paint_area(h=height, w=width, c=coverage):
    result = math.ceil((h * w) / c)
    return result


print(f"You'll need {paint_area()} cans of paint")
