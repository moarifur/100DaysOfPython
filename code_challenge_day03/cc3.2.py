"""
---------------------------------------------------------------------------
Day03: Control Flow and Logical Operators[Beginner]
Code Challenge 3.2: BMI Calculator 2.0
Things to learn:
    - Variable, input function, type casting
    - math function: pow(base, exponent)
    - conditionals: if, elif and else
    - Comparison Operator
    - String formatting: 1 decimal places, string literals
---------------------------------------------------------------------------
"""
import math

print('BMI calculator 2.0')
weight = float(input("Type your weight in kg(Kilogram)\n"))
height = float(input("Type your height in m(Meter)\n"))

bmi = weight/math.pow(height, 2)

if bmi < 18.5:
    print(f'As your bmi is {bmi:.1f}, you are underweight')
elif 18.5 < bmi < 25:
    print(f'As your bmi is {bmi:.1f}, you have a normal weight')
elif 25 < bmi < 30:
    print(f'As your bmi is {bmi:.1f}, you are overweight')
elif 30 < bmi < 35:
    print(f'As your bmi is {bmi:.1f}, you are obese')
elif bmi > 35:
    print(f'As your bmi is {bmi:.1f}, you are clinically obese')
