"""
---------------------------------------------------------------------------
Day06: Python Functions & Karel[Beginner]
Code Challenge 6.1: Reeborg's World Hurdles-1 Challenge
Game URL: https://tinyurl.com/c59bf6km
Things to learn:
    - for-in loop
    - Create a function: def function_name():
*** Put/ open this code to the python code console in the game dashboard
---------------------------------------------------------------------------
"""


def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


for x in range(0, 6):
    jump()
