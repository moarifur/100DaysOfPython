"""
---------------------------------------------------------------------------
Day05: Python Loops[Beginner]
Code Challenge 5.1: Calculate Average Height
Things to learn:
    - list
    - List Method: len()
    - for-in loop
    - Math Module: math.ceil()
---------------------------------------------------------------------------
"""
import math

print('Calculate Average Height')
student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
for height in student_heights:
    total_height += height

print(f'The average height is: {math.ceil(total_height/len(student_heights))}')

